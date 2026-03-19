import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Churn Prediction", layout="centered")

st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

try:
    model = joblib.load("churn_model.pkl")
except Exception as e:
    st.error(f"Model failed to load: {e}")
    st.stop()

# Sidebar
st.sidebar.header("About")
st.sidebar.write("This app uses an optimized ML model to predict customer churn.")

# ------------------------
# Input Section
# ------------------------

st.subheader("Customer Information")

gender = st.selectbox("Gender", ["Male", "Female"])

# FIXED: Senior Citizen mapping
senior_citizen = st.selectbox(
    "Senior Citizen",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure (months)", 0, 72, 12)

phone_service = st.selectbox("Phone Service", ["Yes", "No"])

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# ------------------------
# Prediction
# ------------------------

if st.button("Predict"):

    input_df = pd.DataFrame({
        "gender":[gender],
        "senior_citizen":[senior_citizen],
        "partner":[partner],
        "dependents":[dependents],
        "tenure":[tenure],
        "phone_service":[phone_service],
        "multiple_lines":[multiple_lines],
        "internet_service":[internet_service],
        "online_security":[online_security],
        "online_backup":[online_backup],
        "device_protection":[device_protection],
        "tech_support":[tech_support],
        "streaming_tv":[streaming_tv],
        "streaming_movies":[streaming_movies],
        "contract":[contract],
        "paperless_billing":[paperless_billing],
        "payment_method":[payment_method],
        "monthly_charges":[monthly_charges],
        "total_charges":[total_charges]
    })

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("Result")

    # Convert to %
    prob_percent = prob * 100

    if prob > 0.5:
        st.error(f" High Risk of Churn ({prob_percent:.2f}%)")
    elif prob > 0.2:
        st.warning(f" Medium Risk of Churn ({prob_percent:.2f}%)")
    else:
        st.success(f" Low Risk (Likely to Stay) ({prob_percent:.2f}%)")
