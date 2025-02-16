# import streamlit as st
# from prediction_helper import predict
# from xgboost import XGBRegressor
# import sklearn
#
# # Define the page layout
# st.title('Health Insurance Cost Predictor')
#
# categorical_options = {
#     'Gender': ['Male', 'Female'],
#     'Marital Status': ['Unmarried', 'Married'],
#     'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
#     'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
#     'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
#     'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
#     'Medical History': [
#         'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
#         'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
#         'Diabetes & Heart disease'
#     ],
#     'Insurance Plan': ['Bronze', 'Silver', 'Gold']
# }
#
# # Create four rows of three columns each
# row1 = st.columns(3)
# row2 = st.columns(3)
# row3 = st.columns(3)
# row4 = st.columns(3)
#
# # Assign inputs to the grid
# with row1[0]:
#     age = st.number_input('Age', min_value=18, step=1, max_value=100)
# with row1[1]:
#     number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
# with row1[2]:
#     income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
#
# with row2[0]:
#     genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
# with row2[1]:
#     insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
# with row2[2]:
#     employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
#
# with row3[0]:
#     gender = st.selectbox('Gender', categorical_options['Gender'])
# with row3[1]:
#     marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
# with row3[2]:
#     bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
#
# with row4[0]:
#     smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
# with row4[1]:
#     region = st.selectbox('Region', categorical_options['Region'])
# with row4[2]:
#     medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
#
# # Create a dictionary for input values
# input_dict = {
#     'Age': age,
#     'Number of Dependants': number_of_dependants,
#     'Income in Lakhs': income_lakhs,
#     'Genetical Risk': genetical_risk,
#     'Insurance Plan': insurance_plan,
#     'Employment Status': employment_status,
#     'Gender': gender,
#     'Marital Status': marital_status,
#     'BMI Category': bmi_category,
#     'Smoking Status': smoking_status,
#     'Region': region,
#     'Medical History': medical_history
# }
#
# # Button to make prediction
# if st.button('Predict'):
#     prediction = predict(input_dict)
#     st.success(f'Predicted Health Insurance Cost: {prediction}')

import streamlit as st
from prediction_helper import predict
from xgboost import XGBRegressor
import sklearn

# Define the page layout
st.title('🏥Health Insurance Cost Predictor🔍')

# st.markdown("### 🔍 Enter your details below to get your estimated premium!")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('🧑 Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧 Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('💰 Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk (0-5)', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('🛡️ Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('⚧️ Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('🌎 Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Predict Button with Animated Pop-up
if st.button('🚀 Predict Premium'):
    with st.spinner("⏳ Calculating your premium..."):
        prediction = predict(input_dict)

    # 🔔 Show subtle notification
    st.toast("✅ Prediction Completed!", icon="✅")

    # 💰 Display premium amount in a styled format
    st.markdown(f"""
    <div style="text-align:center; padding:20px; background-color:#f0f0f0; 
                border-radius:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h2 style="color:#0073e6;">Your Estimated Health Insurance Premium:</h2>
        <h1 style="color:green; font-size:40px;">₹ {prediction:.2f} </h1>
        <p style="color:#333;">Based on your details, this is an estimate of your annual premium.</p>
    </div>
    """, unsafe_allow_html=True)