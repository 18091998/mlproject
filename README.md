# 🎓 Student Exam Performance Prediction

A production-grade end-to-end Machine Learning web application that predicts a student's **Math Score** based on demographic and academic features.

🌐 **Live Demo:** [https://mlproject-gpyj.onrender.com](https://mlproject-gpyj.onrender.com)

---

## 📌 Problem Statement

Predict the mathematics score of a student based on input features such as gender, ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

---

## 🖥️ Web Application Preview

> Enter student details → Click Predict → Get predicted Math Score instantly

---

## 🔧 Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.8+ |
| ML Libraries | Scikit-learn, XGBoost, CatBoost |
| Web Framework | Flask |
| Deployment | Render + GitHub Actions CI/CD |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |

---

## 🏗️ Project Architecture

```
mlproject/
├── .github/
│   └── workflows/         # CI/CD GitHub Actions pipeline
├── .ebextensions/         # AWS Elastic Beanstalk config
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Data loading & train/test split
│   │   ├── data_transformation.py  # Feature engineering pipeline
│   │   └── model_trainer.py        # Model training & evaluation
│   ├── pipeline/
│   │   ├── predict_pipeline.py     # Prediction pipeline
│   │   └── train_pipeline.py       # Training pipeline
│   ├── logger.py                   # Custom logging system
│   └── exception.py                # Custom exception handling
├── templates/             # Flask HTML templates
├── app.py                 # Flask application
├── application.py         # WSGI entry point
├── requirements.txt
└── setup.py
```

---

## ⚙️ ML Pipeline

### 1. Data Ingestion
- Loads raw dataset (1,000 student records)
- Splits into train (80%) and test (20%) sets automatically

### 2. Data Transformation
- **Numerical features:** StandardScaler normalization
- **Categorical features:** OneHotEncoder
- Built using Scikit-learn ColumnTransformer Pipeline
- Saves preprocessor as `.pkl` for reuse

### 3. Model Training
Trains and evaluates **7 algorithms** with hyperparameter tuning:

| Model | Description |
|---|---|
| Linear Regression | Baseline model |
| Decision Tree | Non-linear splits |
| Random Forest | Ensemble bagging |
| Gradient Boosting | Ensemble boosting |
| XGBoost | Extreme gradient boosting |
| CatBoost | Categorical boosting |
| AdaBoost | Adaptive boosting |

✅ **Best model auto-selected** based on R² score on test set

---

## 📊 Dataset Features

| Feature | Type | Description |
|---|---|---|
| gender | Categorical | Male / Female |
| race_ethnicity | Categorical | Group A-E |
| parental_level_of_education | Categorical | Education level |
| lunch | Categorical | Standard / Free-reduced |
| test_preparation_course | Categorical | Completed / None |
| reading_score | Numerical | Score out of 100 |
| writing_score | Numerical | Score out of 100 |
| **math_score** | **Target** | **Score out of 100** |

---

## 🚀 How To Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/18091998/mlproject.git
cd mlproject
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for automated deployment:

```
Push to main branch
        ↓
GitHub Actions triggered
        ↓
Install dependencies
        ↓
Auto deploy to Render
        ↓
Live app updated ✅
```

---

## 📦 Custom Components

### Logger
```python
# Automatic timestamped log files
from src.logger import logging
logging.info("Data ingestion started")
```

### Exception Handler
```python
# Detailed error tracking with file and line info
from src.exception import CustomException
raise CustomException(e, sys)
```

---

## 👤 Author

**Shubhadeep Ghosh**
- 📧 ghoshshubhadeep18@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/shubhadeep-ghosh-b85623322)
- 🐙 [GitHub](https://github.com/18091998)

---

## ⭐ If you found this project helpful, please give it a star!
