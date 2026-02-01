# 🌱 Smart Crop Recommendation System

## 📌 Overview

The **Smart Crop Recommendation System** is a machine learning–based application designed to help farmers and agricultural stakeholders make data-driven decisions. By analyzing soil nutrients and environmental conditions, the system recommends the most suitable crop and provides insights into fertilizer dependency.

This project aims to improve crop yield, reduce unnecessary fertilizer usage, and promote sustainable farming practices.

---

## 🎯 Objectives

* Recommend the best crop based on soil and environmental parameters
* Predict fertilizer dependency using soil nutrient values (N, P, K)
* Support farmers with intelligent, data-backed decisions
* Encourage efficient and sustainable agriculture

---

## 🧠 Features

* ✅ Crop recommendation using Machine Learning
* ✅ Fertilizer dependency prediction (Low / High)
* ✅ User-friendly interface (Streamlit / Web-based)
* ✅ Fast and accurate predictions
* ✅ Scalable and extendable system

---

## 📊 Input Parameters

The system uses the following inputs:

### 🌾 Crop Recommendation Model

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH value of soil
* Rainfall

### 🧪 Fertilizer Dependency Model

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)

---

## 📤 Output

* 🌱 **Recommended Crop** (e.g., Rice, Wheat, Maize, etc.)
* 🧪 **Fertilizer Dependency**:

  * Low Dependent
  * High Dependent

---

## 🏗️ System Architecture

1. Data Collection
2. Data Preprocessing
3. Model Training
4. Model Evaluation
5. Model Deployment
6. User Interaction

---

## 🤖 Machine Learning Models Used for Tuning

Random Forest Classifier

Support Vector Machine (SVM)

K-Nearest Neighbors (KNN)

After hyperparameter tuning and performance evaluation, the Random Forest Classifier was selected as the final model and trained on the dataset, achieving an accuracy of 96%, making it the most reliable model for crop recommendation.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * NumPy
  * Pandas
  * Matplotlib
  * Scikit-learn
  * Pickle
* **Frontend:** Streamlit
* **IDE:** Jupyter Notebook / VS Code

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-crop-recommendation.git
cd smart-crop-recommendation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Smart-Crop-Recommendation-System/
│
├── Streamlit/                                   # Main Streamlit application
│   ├── app.py                                   
│   ├── requirements.txt                         # Python dependencies
│   ├── model-1.pkl                              # Trained crop recommendation model
│   ├── model-2.pkl                              # Trained fertilizer dependency model
│   └── crop_recommendation_dataset.csv          # Dataset used for training
|   ├── crop.ipynb         
│   └── model-2.ipynb 
│
├── .gitignore                 # Git ignored files
├── README.md                  # Project documentation

```

---

## 📈 Future Enhancements

* 🌍 Weather API integration
* 📱 Mobile-friendly interface
* 🛰️ Real-time soil sensor integration
* 🗺️ Location-based crop suggestions
* 🧠 Deep learning–based prediction

---

## 👩‍💻 Author

**Afeefa S**
Aspiring Python Full Stack Developer/ Data Scientist.


---


⭐ *If you like this project, don’t forget to give it a star on GitHub!*
