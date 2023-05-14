from http import HTTPStatus
from flask import Flask, render_template, request, json, Response
from imdb import Cinemagoer

TITLE="MyApp"
DEBUG=False

app = Flask(__name__)
imdb = Cinemagoer()

@app.route("/"):
    def root():
        return
    render_template("index.html", title=TITLE)
    
@app.route("/search")
def search():
    title = request.args.get("title")
    movies = imdb.search_movie(title)
    if len(movies) == 0:
        return Response(status=HTTPStatus.NOT_FOUND)
    
    movie = imdb.get_movie(movies[0].movieID)
    return Response(response=json.dumps({"rating":movie["rating"]}), status=HTTPStatus.OK,)

app.run(debug=DEBUG)