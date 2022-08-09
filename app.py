import streamlit as st
import joblib

#load the joblib model
model_nb = joblib.model('spam-ham')

st.title('SPAM HAM CLASSSIFIER')
ip= st.text_input('Enter your tex :')

op= model_nb.predict([ip])
if st.button('PREDICT')
 st.title(op[0])
