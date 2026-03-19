# Customer Churn Prediction App

## Project Overview
This is an end-to-end Machine Learning project to predict customer churn.  
The workflow follows a structured pipeline from data preprocessing to model deployment, ensuring both analytical depth and practical usability.

---

## Business Problem
Customer churn directly impacts revenue.  
The goal is to identify customers at high risk of leaving and enable proactive retention strategies.

---

## Dataset
Dataset used: Telco Customer Churn Dataset  
- Contains customer demographics, services, and account details  
- Target variable: **Churn (Yes/No)**  

---

## Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit  
- Matplotlib / Seaborn  

---

## Project Workflow

### 1. Data Cleaning & Preparation
- Removed irrelevant features (customer_id)  
- Converted target variable (Churn → 0/1)  
- Fixed data types (TotalCharges → numeric)  
- Handled missing values  

---

### 2. Data Preprocessing
- Feature separation (numerical & categorical)  
- Applied:
  - StandardScaler (numerical)  
  - OneHotEncoder (categorical)  
- Combined using **ColumnTransformer**  
- Built unified pipelines for each model  

---

### 3. Baseline Model Building
Models trained using pipelines:
- Logistic Regression  
- KNN  
- SVC  
- Decision Tree  
- Random Forest  
- XGBoost  

---

### 4. Baseline Model Evaluation
- Metrics used:
  - Accuracy  
  - Precision  
  - Recall  
  - F1 Score  
  - ROC-AUC  
- ROC Curve comparison performed  

* Logistic Regression showed the strongest baseline performance based on ROC-AUC  

---

### 5. Hyperparameter Tuning
Performed using **RandomizedSearchCV** with cross-validation:

- Logistic Regression  
- Random Forest  
- XGBoost  

Optimized parameters such as:
- Regularization (C)  
- Tree depth  
- Learning rate  
- Number of estimators  
- Class imbalance handling  

---

### 6. Final Model Comparison
- Compared tuned models using ROC-AUC  
- Visualized performance using ROC curves  

* **XGBoost selected as the final model**  

---

## Final Model (XGBoost)

- ROC-AUC: ~0.84  
- Accuracy: ~79%  

**Reason for selection:**
- Best balance between precision and recall  
- Strong ability to capture non-linear relationships  
- High overall predictive performance  

---

## Key Business Insights

- Month-to-month customers show the highest churn risk  
- Fiber optic users have higher churn (possible pricing/service issue)  
- Lack of tech support & security increases churn probability  
- Higher monthly charges correlate with higher churn  

* Indicates pricing sensitivity and service quality are key factors  

---

## How It Works
1. User inputs customer details in the Streamlit app  
2. Data is preprocessed using the trained pipeline  
3. XGBoost model predicts churn probability  
4. Output shows whether the customer is likely to churn  

---

## Deployment
- Model deployed using **Streamlit**  
- Provides real-time churn prediction based on user input  
