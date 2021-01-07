# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:33:54 2021

@author: Justyn
"""

import pandas as pd
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    #to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("finalized_model.pkl","rb"))
    loaded_OHE = pickle.load(open("OH_encoder.pkl","rb"))
    
    df = pd.DataFrame(data=to_predict_list, index = [0])
    cat_list = ['Make', 'BodyStyle', 'Drivetrain','SellerType', 'Reserve', 'Transmission']
    num_data = df.drop(cat_list, axis = 1)
    int_data = num_data.apply(pd.to_numeric)
    cat_data = pd.DataFrame(loaded_OHE.transform(df[cat_list]))

    encoded_data = pd.concat([int_data, cat_data], axis = 1)
    
    result = loaded_model.predict(encoded_data)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        #to_predict_list=list(to_predict_list.values())
        result = ValuePredictor(to_predict_list)
        return render_template("index.html",prediction=result)
    
if __name__ == '__main__':
    app.run()