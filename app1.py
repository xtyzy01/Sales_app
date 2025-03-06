import numpy as np
import pickle
import sklearn

#load the model

with open('AdvSales_model.pkl', 'rb') as file:
    model = pickle.load(file)

import streamlit as st


#streamlit UI
st.title('Sales Prediction App')
st.write('This app estimates the potential revenue a business can generate based on its investment in radio, TV, and social media advertising.')
st.write('Please input the following parameters:')

#Input form
Tv_Amount=st.number_input('TV',min_value=1000.0, max_value=999999.0, value=2000.0)
Radio_Amount=st.number_input('Radio',min_value=1000.0, max_value=999999.0, value=2000.0)
Socialmedia_Amount=st.number_input('Socialmedia',min_value=1000.0, max_value=999999.0, value=2000.0)


#prediction
if st.button('Predict'):
    user_input= np.array([[Radio_Amount, Tv_Amount,Socialmedia_Amount]])
    prediction= model.predict(user_input)
    
    
    #st.write(prediction)
    
    st.write(f'The predicted amount is:{prediction}')
