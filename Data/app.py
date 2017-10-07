from flask import Flask
from flask import request
import requests
from flask import jsonify
# from jinja2 import Environment, PackageLoader, select_autoescape
# import numpy as np
# from datascience import *
# import datetime as dt
#
# # These lines set up graphing capabilities.
# import matplotlib
# #matplotlib inline
# import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight')
# import warnings
# warnings.simplefilter('ignore', FutureWarning)
app = Flask(__name__)

@app.route("/")
def hello():
#     return "Hello World!"
    return article_search(request.args.get('term'), request.args.get('begin'), request.args.get('end'))

def article_extract(article):
    return {'Name': article['headline']['main'],
            'URL': article['web_url'],
            'Date-Time': article['pub_date'] if 'pub_date' in article else ''

    }

def article_search(term, begin, end):
    data_search = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=28ec5f20ab074501b55d83ea93cec91b&q=%s&begin_date=%s&end_date=%s"% (term, begin, end))
    return jsonify(article_extract(data_search.json()['response']['docs'][0]))
