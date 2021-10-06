from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import *
from sqlalchemy import create_engine
import os
from nlp_module.Processor import *
from nlp_module.Modelling import *

model = pickle.load(open("sgd_classifier.pkl",'rb'))
pipe = pickle.load(open("pipe.pkl",'rb'))

app = Flask(__name__)
engine = create_engine('sqlite:///pynlp.db', echo=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file) 
        data_tfidf = pipe.transform(data['Job Title'])
        data['Type'] = model.predict(data_tfidf)
        data.to_sql('Jobs', con=engine, if_exists='fail',index=False)
        qry_table=pd.read_sql_query("SELECT * FROM Jobs", con=engine)
        return qry_table.to_html(header="true", table_id="table")
    
if __name__ == '__main__':
    app.run(port = 1000, debug=True)
    
    



