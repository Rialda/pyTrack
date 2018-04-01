from flask import Flask, render_template, jsonify, Blueprint

app = Flask(__name__)

from src.calls import twitter_call,fb_call, ig_call, g_call

# @ signifies a decorator - for wrapping function and modifying it's behavior
# @ map a url to a return value
@app.route('/')
@app.route('/api/<data_source>')
def index(data_source=None):
    twitter = twitter_call.twitter_api()
    facebook = fb_call.facebook_api()
    instagram = ig_call.instagram_api()
    google = g_call.google_api()
    return render_template("data.html", data_source=data_source, twitter=twitter, facebook=facebook, instagram=instagram, google=google)




@app.route('/terms', methods=['GET'])
def terms():
    return jsonify({'iliLikeTerms':iliLikeTerms})

@app.route('/terms/<string:term>', methods=['GET'])
def returnTerm(term):
    terms = [iliterm for iliterm in iliLikeTerms if iliterm['term'] == term ]
    return jsonify({'term': terms[0]})


iliLikeTerms = [
    {'term': 'flu'},
    {'term': 'influenza'},
    {'term': 'condition'},
    {'term': 'disease'},
    {'term': 'illness'},
    {'term': 'syndrome'},
    {'term': 'epidemic'},
    {'term': 'temperature'},
    {'term': 'fever'},
    {'term': 'infection'},
    {'term': 'ill'},
    {'term': 'virus'},
    {'term': 'complaint'},
    {'term': 'stroke'},
    {'term': 'caugh'},
    {'term': 'attack'},
    {'term': 'infection'},
    {'term': 'sick'},
    {'term': 'sickness'},
    {'term': 'disability'},
    {'term': 'unable'},
    {'term': 'dose'},
    {'term': 'germs'},
    {'term': 'contagious'},
    {'term': 'dehydrated'},
    {'term': 'dehydration'},
    {'term': 'epidemic'},
    {'term': 'fever'},
    {'term': 'immune'},
    {'term': 'incubation'},
    {'term': 'infected'},
    {'term': 'microorganism'},
    {'term': 'mutate'},
    {'term': 'respiratory'},
    {'term': 'breathing'},
    {'term': 'vaccine'},
    {'term': 'medicine'},
    {'term': 'virulent'},
    {'term': 'infestation'},
    {'term': 'invasion'},
    {'term': 'outbreak'},
    {'term': 'pandemic'},
    {'term': 'scourge'},
    {'term': 'rash'},
    {'term': 'ravage'},
    {'term': 'hydra'},
    {'term': 'affliction'},
    {'term': 'pestilence'},
    {'term': 'sniffing'},
    {'term': 'bacteria'},
    {'term': 'sneezing'},
    {'term': 'coughing'},
    {'term': 'ache'},
    {'term': 'mucus'},
    {'term': 'headache'},
    {'term': 'runny nose'},
    {'term': 'stuffed nose'},
    {'term': 'stomach flu'},
    {'term': 'influenza'},
    {'term': 'microbes'},
    {'term': 'cold'},
    {'term': 'sweat'},
    {'term': 'aching joints'},
    {'term': 'shivers'},
    {'term': 'fatigue'},
    {'term': 'exhausted'},
    {'term': 'sore throat'},
    {'term': 'chills'},
    {'term': 'rest'},
    {'term': 'chest pain'},
    {'term': 'short breath'},
    {'term': 'treatment'},
    {'term': 'diarrhea'},
    {'term': 'malaise'},
    {'term': 'poor appetite'},
    {'term': 'puke'},
    {'term': 'vomit'},
    {'term': 'nausea'},
    {'term': 'anxiety'},
    {'term': 'anxious'},
    {'term': 'nervous'},
    {'term': 'dry mouth'}
]


# make sure to start the web server whenever this file is called directly
if __name__ == "__main__":
    app.run(debug=True)
