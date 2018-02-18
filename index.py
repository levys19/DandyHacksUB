from flask import Flask, redirect, render_template, request, url_for
import json, requests
from twit import twit
import NLTK_POS
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

app = Flask(__name__)

def plotpie(values):
    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['#87F971', '#F24D4D', '#70ABEA']
    trace = go.Pie(labels=labels, values=values, marker =dict(colors=colors))
    layout = go.Layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    return plotly.offline.plot(go.Figure(data=[trace], layout=layout), output_type="div")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    # grabs the keyword from the form
    keyword = request.form['key_word']
    searchTwit = twit()
    twit.writeToText(keyword)
    results = twit.search()
    #grab 3 numbers from results
    NLTK_POS.makeSentence(twit.frequency(), keyword)
    return render_template('graph.html', chart=plotpie(results))
