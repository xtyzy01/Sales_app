import numpy as np
import pickle
import sklearn

#load the model

with open('AI specialisation/Adsales_model.pkl', 'rb') as file:
    model = pickle.load(file)

import streamlit as st


#streamlit UI
st.title('Sales Prediction App')
st.write('This app predicts the **Sales** amount!')
st.write('Please input the following parameters:')

#Input form
Radio_Amount=st.number_input('Radio',min_value=1000.0, max_value=999999.0, value=2000.0)
Tv_Amount=st.number_input('TV',min_value=1000.0, max_value=999999.0, value=2000.0)
Socialmedia_Amount=st.number_input('Socialmedia',min_value=1000.0, max_value=999999.0, value=2000.0)


#prediction
if st.button('Predict'):
    user_input= np.array([[Radio_Amount, Tv_Amount,Socialmedia_Amount]])
    prediction= model.predict(user_input)
    
    
    #st.write(prediction)
    
    st.write(f'The predicted amount is:{prediction}')
