from flask import Flask, redirect, render_template, request, url_for
import json, requests
from twit import twit

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    #grabs the keyword from the form
    keyword = request.form['key_word']
    searchTwit = twit()
    twit.search(keyword)
    return render_template('graph.html')
