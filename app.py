import streamlit as st 
import pickle
import numpy as np 

st.set_page_config(layout='wide')

header_html = """
<div style="background: -webkit-linear-gradient(45deg, #FF0000, #FF7F00, #FFFF00, #00FF00, #0000FF, #4B0082, #9400D3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 48px;">
    Singapore Resale Flat Price Prediction
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

with open("label_mapping.pickle",'rb') as f:
    labels = pickle.load(f)

with open('model.pickle',"rb") as f:
    model = pickle.load(f)

with st.form("Enter input details to get resale price"):
    month_1 = st.number_input("Enter the month of sale")
    year_1 = st.number_input("Enter the year of sale")
    lease_commence_date_1 = st.number_input("Enter the lease commence year")
    town_1 = st.text_input("Enter town name")
    block_1 = st.text_input("Enter block code")
    street_name_1 = st.text_input("Enter the street name")
    floor_area_1 = st.number_input("Enter Floor Area in sqm")
    flat_model_1 = st.text_input("Enter flat model")
    storey_from_1 = st.number_input("Enter storey from")
    storey_to_1 = st.number_input("Enter storey to")
    button = st.form_submit_button("Submit details")

if button:
    month_inp = month_1
    town_inp = labels['town_label'][town_1]
    block_inp = labels['block_label'][block_1]
    street_name_inp = labels['street_name_label'][street_name_1]
    floor_area_inp = floor_area_1
    flat_model_inp = labels['flat_model_label'][flat_model_1]
    lease_commence_date_inp = lease_commence_date_1
    year_inp = year_1
    storey_from_inp = storey_from_1
    storey_to_inp = storey_to_1

    resale_price = model.predict([month_inp, town_inp, block_inp, street_name_inp, floor_area_inp, flat_model_inp, lease_commence_date_inp, year_inp, storey_from_inp, storey_to_inp ])

    resale_price = np.round(resale_price, 2)

    st.markdown("<h1 style='color:yellow'>Resale Price</h1>", unsafe_allow_html=True)

    st.write(f"<h2 style='color:green'>{resale_price}</h2>", unsafe_allow_html=True)





