import streamlit as st
import helper
import pickle
import numpy as np
import pandas as pd
import lightgbm as lgb
import nltk
nltk.download('punkt')
nltk.download('stopwords')
model = pickle.load(open('model1.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    # query = helper.query_point_creator(q1,q2)
    result = model.predict_proba(helper.query_point_creator(q1,q2))[:,1][0]
    result=result*100
    result=result.round(decimals=2)
    # if result>0.5:
    st.header(f"The probability for above question pairs to be duplicates is {result} %")
    # else:
    # st.header(result)
    #     st.header('Not Duplicate',result)
# model.predict_proba(helper.query_point_creator(q1,q3))[:,1]