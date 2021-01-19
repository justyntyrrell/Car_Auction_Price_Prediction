# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:33:54 2021

@author: Justyn
"""

import pandas as pd
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def ValuePredictor(to_predict_list):
    # Unserialize XGBoost model and one hot encoder
    loaded_model = pickle.load(open("finalized_model.sav","rb"))
    loaded_OHE = pickle.load(open("OH_encoder.pkl","rb"))
    
    # Create a pandas data from user input 
    df = pd.DataFrame(data=to_predict_list, index = [0])
    # List of categorical features that will be encoded
    cat_list = ['Make', 'BodyStyle', 'Drivetrain','SellerType', 'Reserve', 'Transmission']
    # List of numerical data by removing categorical data
    num_data = df.drop(cat_list, axis = 1)
    # Convert numerical data to integer
    int_data = num_data.apply(pd.to_numeric)
    # One hot encode categorical data
    cat_data = pd.DataFrame(loaded_OHE.transform(df[cat_list]))
    # Combine numerical and categorical data into one data frame
    encoded_data = pd.concat([int_data, cat_data], axis = 1)
    # predict with model 
    result = loaded_model.predict(encoded_data)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)
        return render_template("index.html",prediction=result)
    
if __name__ == '__main__':
    app.run()