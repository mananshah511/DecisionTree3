from flask import Flask, request, jsonify, render_template
import requests
import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


app = Flask(__name__)


@app.route('/', methods= ['GET'])
def homepage():
    return render_template("index.html")


@app.route('/predict', methods = ['POST'])
def predict():
    model3 = pickle.load(open('model3.pkl', 'rb'))
    data = [x for x in request.form.values()]
    if data[5] == 'female':
        data[5] = 1
    else:
        data[5] = 0
    if data[5] == 0:
        data.append(1)
    else:
        data.append(0)
    final_features = [np.array(data)]
    for i in range(len(data)):
        data[i] = float(data[i])
    print(data)
    output = model3.predict(final_features)[0]
    print(output)
    if output == 0:
        return render_template('index.html', prediction_text="This passenger wont survive")
    else:
        return render_template('index.html', prediction_text="This passenger will survive")


if __name__ == "__main__":
    app.run()