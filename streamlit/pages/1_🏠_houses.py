import streamlit as st
import json
import requests

st.title("Predict your price for your house based on the square meters, amount of bedrooms and the Province")

PropertySubType = st.selectbox('Wat type of property do you want to sell?',
           ('Selecte your property type','HOUSE', 'appartment (in progress)'))

st.write('How many square meters is your property?')
LivingArea = st.slider("m2", 0, 600, 1)

st.write('How many bedrooms are there?')
BedroomCount = st.slider("Number of bedrooms", 0, 10, 1)

st.write('In which country is your property located?')
Province = st.selectbox("Province", ('Select Province', 'Antwerp', 'Brussels', 'East Flanders', 'Flemish Brabant', 'Hainaut', 
                                    'Liege', 'Limburg','Luxembourg', 'Namur', 'Walloon Brabant', 
                                    'West Flanders'))

streamlit_input = {"PropertySubType" : PropertySubType, "LivingArea" : LivingArea, "BedroomCount" : BedroomCount,
                   "Province" : Province}

#create button
if st.button('Predict the Price'):
    res = requests.post(url=' https://immo-eliza-deployment-caroline-streamlit.onrender.com/', data = json.dumps(streamlit_input))
    st.header(f'This is the predicted price for your property : {res.text} €')


#http://localhost:8502/houses

#url='http://127.0.0.1:8000/predict/houses'