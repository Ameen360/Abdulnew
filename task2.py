import streamlit as st
import pandas as pd
import random as rd





st.set_page_config(page_title="AppTwo",page_icon=":cyclone:")

st.title("Select a quetion and type your answer")



option = st.selectbox(
   "Answer the following question?",
   ("What is your favourite programming language","What is your best food", \
    "What is the name of your pet","What is the name of the best programming school in Ilorin"),
   
   index=None,
    

   placeholder="Select your answer...",
)

st.write("You selected:", option)



title = st.text_input("Type your Answer",)
st.write(title)


submit_btn = st.button("Submit")

def submit():
    st.header(
        f" your answer is {title}" )
    
if submit_btn:
    submit()
    