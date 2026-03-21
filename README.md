# Customer Churn Prediction

## Project Overview
An end-to-end Machine Learning project to predict customer churn using multiple classification models.  
The project covers data preprocessing, model training, evaluation, and business insights generation.

---

## Business Problem
Customer churn directly impacts revenue.  
The goal is to identify high-risk customers and support retention strategies.

---

## Workflow
1. Data Cleaning & Preparation  
2. Exploratory Data Analysis (EDA)  
3. Data Preprocessing (Encoding, Scaling, Train-Test Split)  
4. Model Training (Logistic Regression, Random Forest, XGBoost)  
5. Hyperparameter Tuning  
6. Model Evaluation & Selection  
7. Feature Importance Analysis  

---

## Model Pipeline
- Used ColumnTransformer to handle numerical and categorical features  
- Applied StandardScaler for numerical features  
- Applied OneHotEncoder for categorical features  
- Built pipelines using Scikit-learn Pipeline  
- Saved trained model using joblib  

---

## Final Model
- XGBoost selected as final model  
- ROC-AUC: ~0.84  
- Accuracy: ~79%  

---

## Key Insights
- Month-to-month customers show higher churn risk  
- Fiber optic users more likely to churn  
- High monthly charges increase churn probability  

---

## Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn, XGBoost  
- Matplotlib, Seaborn  
- Streamlit  

---

## Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt
streamlit run app.py



