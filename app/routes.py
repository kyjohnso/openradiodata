from flask import render_template, url_for, jsonify
from app import app

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title="Open Radio Data")

@app.route('/raw/', methods=['GET', 'POST'])
def raw():
    return "no raw data"    
    
