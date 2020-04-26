import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

# Declare a flask app
app = Flask(__name__)

print('App loaded.')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])

def predict():
    if request.method == 'POST':
        # Get the image from post request
        ans_mode = "Flask is more important than model!! Dang!"
        return jsonify(result=str(ans_mode))
    return None

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="66", threaded=False)
