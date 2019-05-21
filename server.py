import numpy as np
from numpy import random
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home_page():
    print('Someone is visiting the homepage. Woop!')
    return 'Good morning, ada!'

@app.route('/roll-dice')
def roller():
    return render_template('index.html', die=str(np.random.randint(1, 6)))

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting.html', greeting=greeting)




