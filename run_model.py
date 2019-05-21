from flask import Flask
from flask import render_template
from flask import request
from model import predict

app = Flask(__name__)

@app.route('/')
def model_home_page():
    print('Someone is visiting the homepage. Woop!')
    return render_template('model-form-exercise.html')

@app.route('/make-prediction', methods=['POST'])
def handle_form_submission():
    text = request.form['text']
    prediction = predict(text)
    print('Someone is predicting on the model.')
    return render_template('prediction.html', prediction=prediction)
