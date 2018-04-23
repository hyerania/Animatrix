from flask import render_template, request, jsonify, url_for
from app import app
import cPickle as pickle
import os
import scipy as sp
import scipy.sparse
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from surprise import SVD
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
from surprise import Dataset
from surprise import Reader
from surprise import accuracy
from datetime import datetime

def now():
    return str(datetime.now())

infile = open('rating.csv', 'r')
outfile = open('ratingSubset.csv', 'w')

for i in range(1000000):
    outfile.write(infile.readline())


infile.close()
outfile.close()

anime_id_name = {
    '32281' : "Kimi no Na wa.",
    '5114' : "Fullmetal Alchemist: Brotherhood",
    '9253' : "Steins;Gate",
    '918' : "Gintama",
    '32935' : "Haikyuu!!: Karasuno Koukou VS Shiratorizawa Gakuen Koukou",
    '1535' : "Death Note",
    '11061' : "Hunter x Hunter (2011)",
    '2904' : "Code Geass: Hangyaku no Lelouch R2"
}

@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/author')
def author():
    # Renders author.html.
    return render_template('author.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/api/animes/ratings', methods=['POST'])
def submit_ratings():
    anime_ratings = request.form
    infile = open('ratingSubset.csv', 'a')
    user_id = "-1"
    for key, value in anime_ratings.iteritems():
        anime_id = key
        rating = value
        infile.write("{}, {}, {}\n".format(user_id, anime_id, rating))
    infile.close()

    ratingSubset = pd.read_csv('ratingSubset.csv')
    ratingSubset["rating"] = ratingSubset["rating"].replace(to_replace = -1, value = 5)

    reader = Reader(rating_scale=(1, 10))
    ratingSubset = Dataset.load_from_df(ratingSubset[['user_id', 'anime_id', 'rating']], reader)
    trainingRatingSubset, testRatingSubset = train_test_split(ratingSubset, test_size=0.01)
    algo = SVD(n_factors = 50, reg_all = 0.05)
    print "{}: Beginning SVD training...".format(now())
    algo.fit(trainingRatingSubset)
    print "{}: End SVD training...".format(now())

    predict_list = [
        820,
        4181,
        263,
        1,
        28891,
        199,
        23273,
        24701,
        12355,
        1575,
        44,
        30276,
        164,
        7311,
        17074,
        21939,
        457,
        2001,
        245,
        32983,
        5258,
        28957,
        11665,
        431,
        11741,
        31757,
        19,
        12365,
        32366,
        30654,
        20583,
        19647,
        4282,
        10379,
        22135,
        21329,
        31043,
        7785,
        3297,
        30709,
        6114,
        31240,
        4565,
        5300,
        9989,
        24415,
        11577,
        10408,
        28171,
        32995,
    ]

    results = []
    for anime_id in predict_list:
        pred = algo.predict(-1, anime_id, verbose=True)
        result = {}
        result['anime_id'] = anime_id
        result['rating'] = pred.est
        results.append(result)
        
    results = sorted(results, key = lambda x: x['rating'], reverse=True)
    return jsonify(success=True, data = results)