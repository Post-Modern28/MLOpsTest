# web_app.py
import streamlit as st
import requests

st.title('ML Model Prediction')

# Input fields
input_data = st.text_input('Enter data (comma-separated):', '5.1,3.5,1.4,0.2')

if st.button('Predict'):
    # Prepare data for API request
    input_data = [float(x) for x in input_data.split(',')]
    response = requests.post('http://api:8000/predict', json={'data': input_data})
    print(f'returned result: {response}')
    result = response.json()

    st.write(f"Prediction: {result['prediction']}")
