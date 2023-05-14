from flask import Flask, render_template, request
from imdb import Cinemagoer
import requests
import re
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template("D:\Documents\School\PP\IMDB-Ratings\index.html")

# Route for processing the form submissionpip
@app.route('/result', methods=['POST'])
def result():
    # Creating IMDb instance
    ia = Cinemagoer()

    # Getting the movie name from the form submission
    name = request.form['movie_name']

    # Searching for the movie
    search = ia.search_movie(name)

    # Fetching movie ID
    movie_id = search[0].getID()

    url = "https://www.imdb.com/title/tt" + movie_id + "/"
    response = requests.get(url, headers={"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.text, "html.parser")

    data = json.loads(soup.find("script", type="application/ld+json").text)

    # Fetching ratings from IMDb
    rating = data["aggregateRating"]["ratingValue"]

    # Fetching ratings from Rotten Tomatoes
    url_rt = "https://www.rottentomatoes.com/m/" + name.replace(' ', '_')
    response = requests.get(url_rt, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.text, "html.parser")

    data = json.loads(soup.find("script", type="application/ld+json").text)

    rating2 = data["aggregateRating"]["ratingValue"]

    # Render the result template with the ratings
    return render_template('result.html', name=name, imdb_rating=rating, rt_rating=rating2)

if __name__ == '__main__':
    app.run()
