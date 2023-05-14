from imdb import Cinemagoer
import requests
import re 
from bs4 import BeautifulSoup
import json

# making imdb instance
ia = Cinemagoer()

#entering the name of the movie
name = str(input("Enter name of the movie: "))

#searching the movie
search = ia.search_movie(name)

# fetching movie ID
movie_id = search[0].getID()

print(movie_id)

url = "https://www.imdb.com/title/tt" + movie_id + "/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")

data = json.loads(soup.find("script", type="application/ld+json").text)

# printing ratings from IMDB
rating = data["aggregateRating"]["ratingValue"]
print(rating)


# fetching ratings from rottentomatoes
url_rt = "https://www.rottentomatoes.com/m/" + name.replace(' ', '_')
response = requests.get(url_rt, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")

data = json.loads(soup.find("script", type="application/ld+json").text)

rating2 = data["aggregateRating"]["ratingValue"]

# printing ratings from rottentomatoes

print(rating2 + '%')