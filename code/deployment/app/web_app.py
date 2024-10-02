# web_app.py
import streamlit as st
import requests


st.title('Wine Recognition Model')


input_fields = []
parameters = 'Alcohol,Malic Acid,Ash,Alcalinity of Ash,Magnesium,Total Phenols,Flavanoids,Nonflavanoid Phenols,Proanthocyanins,'\
'Colour Intensity,Hue,OD280/OD315 of diluted wines,Proline'.split(',')
for i in range(13):
    value = st.text_input(f'{parameters[i]}:', '0.5', key=f'param_{i}')
    input_fields.append(value)

if st.button('Predict'):

    try:
        input_data = [float(x) for x in input_fields]

        response = requests.post('http://api:8000/predict', json={'data': input_data})
        print(f'returned result: {response}')

        result = response.json()

        st.write(f"Prediction: {result['prediction']}")
    except ValueError:
        st.error("Please enter valid numeric values for all parameters.")
