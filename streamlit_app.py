import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# from PIL import Image


pickle_in = open("ads.pkl","rb")
ads_model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_authentication(tv, radio, newspaper):   
    prediction=ads_model.predict([[tv, radio, newspaper]])
    return prediction



def main():
    html_temp = """
    <div style="background-color:transparent;margin:auto">
    <h2 style="color:tomato;text-align:center;">Streamlit 'Sales based on Advertising'</h2>
    <p style="color:olive; text-align:center;">Project 2️⃣<br>
    This is my 2<sup>nd</sup> project. This app analysis the Sales performance based on Advertising in different platforms</p>
    </div>
    <br>
    <br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    tv = st.number_input("Investment on 📺(Tv) advertisements [1000$]",min_value=0, step=1)
    radio = st.number_input("Investment on 📻(Radio) advertisements [1000$]",min_value=0, step=1)
    newspaper = st.number_input("Investment on 📰(Newspaper) advertisements [1000$]",min_value=0, step=1)
    result=""
    if st.button("Predict"):
        result=predict_authentication(tv, radio, newspaper)
    st.success('Sales Revenue in {}M$'.format(result.round(2)))
    if st.button("About Me"):
        st.text("I'm Seetha Jagan")
        st.text("Follow me on 👇")
        st.markdown(
                    "<a href='https://www.linkedin.com/in/seethajagan' target='_blank' style='color:royalblue; text-decoration:none; font-size:18px;'>Linked In</a>",
            unsafe_allow_html=True
        )

if __name__=='__main__':
    main()
