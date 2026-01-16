import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)

# ================= ADVANCED STYLING =================
st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #2e7d32, #66bb6a);
    padding: 30px;
    border-radius: 16px;
    color: white;
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 25px;
}

.sub-text {
    font-size: 18px;
    opacity: 0.9;
}
.crop-card {
    background: white;
    border: 2px solid #2e7d32;
    padding: 16px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #2e7d32;
}

.fert-good {
    background: #e8f5e9;
    border-left: 6px solid #2e7d32;
    padding: 18px;
    font-size: 20px;
    font-weight: 700;
    color: #2e7d32;
    border-radius: 10px;
}

.fert-bad {
    background: #ffebee;
    border-left: 6px solid #c62828;
    padding: 18px;
    font-size: 20px;
    font-weight: 700;
    color: #c62828;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ================= CONSTANTS =================
SOIL_COLUMNS = [
    'Acidic Soil',
    'Alkaline Soil',
    'Loamy Soil',
    'Neutral Soil',
    'Peaty Soil'
]

FEATURE_COLUMNS = [
    'Temperature', 'Humidity', 'Rainfall', 'PH',
    'Nitrogen', 'Phosphorous', 'Potassium', 'Carbon',
    'Acidic Soil', 'Alkaline Soil', 'Loamy Soil',
    'Neutral Soil', 'Peaty Soil'
]

# ================= LOAD MODELS =================
@st.cache_resource
def load_models():
    # Get folder where app.py is located
    folder = os.path.dirname(os.path.abspath(__file__))
    
    model1_path = os.path.join(folder, "model-1.pkl")
    model2_path = os.path.join(folder, "model-2.pkl")
    
    # Check if files exist (optional, helps debug on Cloud)
    if not os.path.exists(model1_path):
        st.error(f"Error: {model1_path} not found!")
    if not os.path.exists(model2_path):
        st.error(f"Error: {model2_path} not found!")

    with open(model1_path, "rb") as f:
        crop_model, label_encoder = pickle.load(f)

    with open(model2_path, "rb") as f:
        fert_model = pickle.load(f)

    return crop_model, fert_model, label_encoder


crop_model, fert_model, label_encoder = load_models()

# ================= PREDICTION =================
def recommend_crops(user_df):
    user_df = user_df[FEATURE_COLUMNS]
    probs = crop_model.predict_proba(user_df)
    top5_idx = np.argsort(probs[0])[-5:][::-1]
    return label_encoder.inverse_transform(top5_idx)

# ================= HEADER =================
st.markdown("""
<div class="main-header">
    🌱 Smart Crop Recommendation System
    <div class="sub-text">
        AI-powered crop & fertilizer guidance for farmers
    </div>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR INPUT =================
st.sidebar.header("🌾 Input Parameters")

N = st.sidebar.slider("Nitrogen (N)", 0, 150, 60)
P = st.sidebar.slider("Phosphorous (P)", 0, 150, 40)
K = st.sidebar.slider("Potassium (K)", 0, 150, 40)
carbon = st.sidebar.slider("Carbon", 0.0, 5.0, 1.2)

temp = st.sidebar.slider("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 70.0)
rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 500.0, 200.0)
ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)

selected_soil = st.sidebar.selectbox("Soil Type", SOIL_COLUMNS)

# ================= BUTTON =================
if st.sidebar.button("🌾 Get Recommendation", use_container_width=True):

    soil_encoding = {col: 0 for col in SOIL_COLUMNS}
    soil_encoding[selected_soil] = 1

    user_input = pd.DataFrame([{
        'Temperature': temp,
        'Humidity': humidity,
        'Rainfall': rainfall,
        'PH': ph,
        'Nitrogen': N,
        'Phosphorous': P,
        'Potassium': K,
        'Carbon': carbon,
        **soil_encoding
    }])

    crops = recommend_crops(user_input)
    fert_result = fert_model.predict(
        user_input[['Nitrogen', 'Phosphorous', 'Potassium']]
    )[0]

    st.subheader("🌱 Top 5 Crop Recommendations")

    left_space, content = space, content = st.columns([0.2, 5]) # adjust ratio if needed

    with content:
        for i, crop in enumerate(crops, start=1):
            st.markdown(f"**{i}. {crop}**")


    st.subheader("🧪 Fertilizer Requirement")

    fert_map = {0: "Highly Dependent", 1: "Low Dependent"}

    # Get model prediction (0 or 1)
    fert_result = fert_model.predict(
        user_input[['Nitrogen', 'Phosphorous', 'Potassium']]
    )[0]

    if fert_result == 0:
        st.error("Highly Dependent on Fertilizers")
    else:
        st.success("Low Fertilizer Dependency")
