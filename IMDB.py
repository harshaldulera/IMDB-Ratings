from imdb import Cinemagoer
import requests
import re
from bs4 import BeautifulSoup

# making imdb instance
ia = Cinemagoer()

#entering the name of the movie
name = str(input("Enter name of the movie: "))

#searching the movie
search = ia.search_movie(name)

movie_id = search[0].getID()

print(movie_id)

url = "https://www.imdb.com/title/tt" + movie_id
response = requests.get(url)
soup = BeautifulSoup(response, "html.parser")
print(soup)

# if not search:
#     print("No results found")
# else:
#     print("ID of the first result", search[0].getID())
