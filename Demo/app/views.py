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

@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')