from newsapi import NewsApiClient
from flask import jsonify

newsapi = NewsApiClient(api_key='4f3a2f68ac6c4de88cda6999cd7c25a9')

def google_api():
    return jsonify(newsapi.get_everything(q='influenza'))


# 4f3a2f68ac6c4de88cda6999cd7c25a9