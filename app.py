from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Udacity Project 5 - By Soumitra Singh </h1>'

app.run(host='0.0.0.0', port=81)