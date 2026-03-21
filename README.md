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
4. Base Model Training(SVC,KNN,Logistic Regression , Decision Tree, XgboostClassifier, Random Forest)
5. Model Comaprison (ROC - AUC plot)
6. Selected Model Training (Logistic Regression, Random Forest, XGBoost)
7. Hyperparameter Tuning
8. Selected Model Comaprison (ROC - AUC plot)
9. Model Evaluation & Selection  
10. Feature Importance Analysis
11. Buissness Insight
12. Future Improvement

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
## Deployment Status
- The application was built and tested locally using Streamlit.
- Deployment was attempted but not completed due to environment compatibility issues.
  
---

## App Preview

### Input Form 1

<img width="700" height="400" alt="Screenshot input2" src="https://github.com/user-attachments/assets/739d04c5-1678-43d9-8a30-035daabdf0cb" />

### Input Form 2

<img width="700" height="400" alt="Screenshot inputs" src="https://github.com/user-attachments/assets/302f48d2-86f1-456b-a08b-47ee96672c86" />

### Prediction Result of Stay

<img width="700" height="400" alt="likely_to_stay_predict" src="https://github.com/user-attachments/assets/d068dd26-5fab-4c54-9373-0150331db963" />

### Prediction Result of Risk 

<img width="700" height="400" alt="churning_risk" src="https://github.com/user-attachments/assets/8444e5d6-83d8-43c3-a7b1-e1a64010c971" />
---

## Run Locally

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt
streamlit run app.py



