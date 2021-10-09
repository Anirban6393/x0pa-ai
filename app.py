import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import *
from nlp_module.Processor import *

engine = create_engine('sqlite:///pynlp.db', echo=False)


model = pickle.load(open("sgd_classifier.pkl",'rb'))
pipe = pickle.load(open("pipe.pkl",'rb'))

file = st.file_uploader("Choose a file", type=["csv","xlsx"])

if st.button('go!'):
        
    all_sheet = pd.ExcelFile(file)   
    sheets = all_sheet.sheet_names

    for i in range(len(sheets)):
        df = pd.read_excel(file, sheet_name = sheets[i])
        df_tfidf = pipe.transform(df['Job Title'])
        df['Type'] = model.predict(df_tfidf)
        st.dataframe(df)
        #df.to_sql('Jobs', con=engine, if_exists='append',index=False)


query = st.text_input("Type SQL Query")
if st.button('search results!'):
    st.write(query)
    qry_data=pd.read_sql_query(query, con=engine)
    st.dataframe(qry_data)
        
    



