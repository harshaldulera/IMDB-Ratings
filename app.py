from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

def fetch_ratings(request):
    if request.method == 'POST':
        movie_title = request.POST.get('movieTitle')
        # Perform your IMDB rating fetching logic here
        # ...
        # Example code to fetch the rating
        url = "https://www.imdb.com/title/tt" + movie_id + "/"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
        soup = BeautifulSoup(response.text, "html.parser")
        data = json.loads(soup.find("script", type="application/ld+json").text)
        rating = data["aggregateRating"]["ratingValue"]
        
        return render(request, 'ratings.html', {'movieTitle': movie_title, 'rating': rating})
    else:
        return render(request, 'ratings.html')
