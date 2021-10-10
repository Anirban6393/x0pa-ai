import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine
from nlp_module.Processor import *

engine = create_engine('sqlite:///pynlp.db', echo=False)
model = pickle.load(open("sgd_classifier.pkl",'rb'))
pipe = pickle.load(open("pipe.pkl",'rb'))

files = st.file_uploader("Choose a file", type=["xlsx"], accept_multiple_files=True)

if st.button('go!'):
    li=[]
    for file in files:
        all_sheet = pd.ExcelFile(file)   
        sheets = all_sheet.sheet_names       
        for i in range(len(sheets)):
            data = pd.read_excel(file, sheet_name = sheets[i])
            li.append(data)
            
    df = pd.concat(li, axis=0, ignore_index=True)
    df_tfidf = pipe.transform(df['Job Title'])
    df['Type'] = model.predict(df_tfidf)
    st.dataframe(df)
    #df.to_sql('Jobs', con=engine, if_exists='append',index=False)



query = st.text_input("Type SQL Query")
if st.button('search results!'):
    st.write(query)
    qry_data=pd.read_sql_query(query, con=engine)
    st.dataframe(qry_data)
        
    



