import os
import sys
import logging


import numpy as np
from flask import Flask, render_template, request, Response, redirect, jsonify 
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.json_util import dumps

from preprocessing import extract_fbanks
from predictions import get_embeddings, get_cosine_distance

app = Flask(__name__)

# Set-up MongoDB Connection
app.config["MONGO_URI"] = "mongodb+srv://ranjeet:ranjeet@cluster0.yh6ehm9.mongodb.net/devesh?retryWrites=true&w=majority"
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

DATA_DIR =r'C:\\Users\\Sparky\\OneDrive\\Desktop\\Major Project\\Attendance-System-Voice-Based-master\\data_files//'
THRESHOLD = 0.45    
# play with this value,so you may get better results

sys.path.append('..')


@app.route('/')
def home():
    return render_template('front.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    username = data['username']

    # Your machine related logic
    # filename = _save_file(request, username)
    # fbanks = extract_fbanks(filename)
    # embeddings = get_embeddings(fbanks)
    # mean_embeddings = np.mean(embeddings, axis=0)
    # np.save(DATA_DIR + username + '/embeddings.npy', mean_embeddings)

    result = mongo.db.users.insert_one({'username': username, 'email': data['email'], 'password': hashed_password})
    user_id = result.inserted_id
    # return redirect('../') # Redirecting to front.html after successful registration
    return render_template('front.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    user = mongo.db.users.find_one({'email': data['email']})
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        # Your machine related logic
        # filename = _save_file(request, username)
        # fbanks = extract_fbanks(filename)
        # embeddings = get_embeddings(fbanks)
        # stored_embeddings = np.load(DATA_DIR + username + '/embeddings.npy')
        # stored_embeddings = stored_embeddings.reshape((1, -1))

        # distances = get_cosine_distance(embeddings, stored_embeddings)
        # positives = distances < THRESHOLD
        # positives_mean = np.mean(positives)
        return render_template('index.html')
    else:
        return jsonify({'error': 'Invalid email or password'}), 401
        # return jsonify({'front.html'}), 




# ({"message": "Invalid email or password"}),401


def _save_file(request_, username):
    file = request_.files['file']
    dir_ = DATA_DIR + username
    if not os.path.exists(dir_):
        os.makedirs(dir_)

    filename = DATA_DIR + username + '/sample.wav'
    file.save(filename)
    return filename

@app.route('/login-attendance/<string:username>', methods=['POST'])
def loginAttendance(username):

    filename = _save_file(request, username)
    fbanks = extract_fbanks(filename)
    embeddings = get_embeddings(fbanks)
    stored_embeddings = np.load(DATA_DIR + username + '/embeddings.npy')
    stored_embeddings = stored_embeddings.reshape((1, -1))

    distances = get_cosine_distance(embeddings, stored_embeddings)
    print('mean distances', np.mean(distances), flush=True)
    positives = distances < THRESHOLD
    positives_mean = np.mean(positives)
    print('positives mean: {}'.format(positives_mean), flush=True)
    if positives_mean >= 0.58:
        return Response('SUCCESS', mimetype='application/json')
    else:
        return Response('FAILURE', mimetype='application/json')


@app.route('/register-attendance/<string:username>', methods=['POST'])
def registerAttendance(username):
    filename = _save_file(request, username)
    fbanks = extract_fbanks(filename)
    embeddings = get_embeddings(fbanks)
    print('shape of embeddings: {}'.format(embeddings.shape), flush=True)
    mean_embeddings = np.mean(embeddings, axis=0)
    np.save(DATA_DIR + username + '/embeddings.npy', mean_embeddings)
    return Response('', mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)

