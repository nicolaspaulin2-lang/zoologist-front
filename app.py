import streamlit as st
import requests

"""
# Penguin Guessr
"""

st.markdown(
    """
#### Fill in the following fields with your penguin details in order to predict its' species:
"""
)

island = st.text_input('Island', 'Biscoe')
bill_length = st.number_input('Bill length (in mm)')
bill_depth = st.number_input('Bill depth (in mm)')
flipper_length = st.number_input('Flipper length (in mm)')
body_mass = st.number_input('Body mass (in g)')
sex = st.text_input('Sex', 'Male or Female')

url = 'http://localhost:8001/predict'

params = {
    'island': island,
    'bill_length_mm': bill_length,
    'bill_depth_mm': bill_depth,
    'flipper_length_mm': flipper_length,
    'body_mass_g': body_mass,
    'sex': sex
}

response = requests.get(url, params=params).json()

st.write('Your penguin is a', response['prediction'],'!')
