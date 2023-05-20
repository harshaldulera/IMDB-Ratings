from flask import Flask, render_template, request, redirect
from imdb import Cinemagoer
import requests
import re
from bs4 import BeautifulSoup
import json

# Creating IMDb instance
ia = Cinemagoer()

# Getting the movie name from the form submission
name = input("Enter name of the movie")

# Searching for the movie
search = ia.search_movie(name)

# Fetching movie ID
movie_id = search[0].getID()

url = "https://www.imdb.com/title/tt" + movie_id + "/"
response = requests.get(url, headers={"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")
 # Raise an exception if there is a 4xx or 5xx status code

data = json.loads(soup.find("script", type="application/ld+json").text)

# Fetching ratings from IMDb
rating = data["aggregateRating"]["ratingValue"]

# Fetching ratings from Rotten Tomatoes
url_rt = "https://www.rottentomatoes.com/m/" + name.replace(' ', '_')
response = requests.get(url_rt, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")

data = json.loads(soup.find("script", type="application/ld+json").text)

rating2 = data["aggregateRating"]["ratingValue"]

print(movie_id)
print(rating)
print(rating2)