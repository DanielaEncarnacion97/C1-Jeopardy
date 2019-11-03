import requests
import json
import pprint
from flask import Flask, render_template, jsonify, request


# gives users the ability to refine search results by:
# date or timeframe aired (you can search by a day,  a week, a month)
# trivia category
# level of difficulty of the question
# any other smart searching criteria you see fit

# route me to the root / homepage

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    params = {
        
    }
    url = "http://jservice.io/api/clues"
    response = requests.get(url)
    response_json = response.json()
    # res = json.dumps(response.text, sort_keys = False, indent = 2)
    # pprint.pprint(res)
    return render_template('index.html',len = len(response_json), response=response_json)

#     return '''
#         <html>
#     <head>
#     </head>
#     <body>
#         <h1>response_json[question]</h1>
#         response
#     </body>
# </html>
#     '''





# def get_values(value):
#     params = {
#         'value': value
#     }
#     response = requests.get(url, params=params)
#     response_json = response.json()
#     # pprint.pprint(response_json)
#     return response_json

# response_json[0]

# print(get_values(100)[0]['answer'])
# print(get_values(100)[0]['value'])
# print(get_values(100)[0]['category']['title'])



if __name__ == "__main__":
		app.run(debug=True)

