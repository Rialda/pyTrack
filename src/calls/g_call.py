from newsapi import NewsApiClient
from flask import jsonify
from scipy import stats
#newsapi = NewsApiClient(api_key='4f3a2f68ac6c4de88cda6999cd7c25a9')

def google_api():
    #return jsonify(newsapi.get_everything(q='influenza'))
    return stats.pearsonr([13.131,
    11.047,
    20.383,
    15.385,
    18.444,
    14.912,
    16.438,
    14.667,
    15.918,
    14.875,
    22.699,
    18.800,
    17.727,
    20.554,
    18.347,
    18.116,
    15.909,
    17.350,
    10.875,
    8.937,
    10.390,
    15.854,
    14.653,
    15.789,
    7.521,
    11.111
    ], [3.424,
    4.438,
    5.339,
    7.186,
    6.722,
    8.450,
    14.013,
    22.445,
    25.473,
    24.741,
    25.566,
    26.695,
    26.059,
    26.339,
    26.496,
    25.396,
    21.568,
    17.707,
    14.998,
    15.333,
    14.694,
    15.383,
    12.761,
    10.934,
    8.879,
    7.410
    ])



# 4f3a2f68ac6c4de88cda6999cd7c25a9