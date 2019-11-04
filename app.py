import requests
import request
from datetime import datetime
import json
import pprint
from flask import Flask, render_template, jsonify, request


# gives users the ability to refine search results by:
# date or timeframe aired (you can search by a day,  a week, a month)
# trivia category
# level of difficulty of the question
# any other smart searching criteria you see fit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.args.get('startDate'))
    print(request.args.get('endDate'))
    url = "http://jservice.io/api/clues/"
    response = requests.get(url)
    response_json = response.json()    
    # print(response_json)
    return render_template('index.html',len = len(response_json), response=response_json)

@app.route('/search')
def search():
    params = {}

    difficulty = request.args.get('difficulty')
    category = request.args.get('category')

    if difficulty.isdigit():
        params = {
        'min_date': request.args.get('startDate'),
        'max_date': request.args.get('endDate'),
        'category.title' : request.args.get('category'),
        'value': int(request.args.get('difficulty'))
        }
    else:
        params = {
        'min_date': request.args.get('startDate'),
        'max_date': request.args.get('endDate'),
        'category.title' : request.args.get('category')
        }
    
    url = "http://jservice.io/api/clues/"
    response = requests.get(url, params=params)
    response_json = response.json()  
    return render_template('search.html', len = len(response_json), search=response_json, category=category)

@app.route('/random')
def random():
    url = "http://jservice.io/api/random/"
    response = requests.get(url)
    response_json = response.json()  
    return render_template('random.html', len = len(response_json), random=response_json)


if __name__ == "__main__":
		app.run(debug=True)

