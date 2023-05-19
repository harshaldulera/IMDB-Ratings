# Flask Movie Rating App

This Flask application allows you to search for a movie and retrieve its ratings from IMDb and Rotten Tomatoes.

## Prerequisites

- Python 3.6 or higher
- Flask 
- imdbpy 
- requests 
- beautifulsoup4 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/harshaldulera/flask-movie-rating-app.git
   cd flask-movie-rating-app

2.  Install the required Dependencies

    ```pip install -r requirements.py

3. Run the Flask Application:

    ```python app
The application will be accessible at https://localhost:5000/

## Usage

1. Open your web browser and go to http://localhost:5000.
2. Enter the name of the movie you want to search for in the provided input field.
3. Click the "Search" button.
4. The application will retrieve the movie's ratings from IMDb and Rotten Tomatoes.
5. The ratings will be displayed on the result page.

## Error Handling

If the requrest to IMDb or Rotten Tomaotes returns a 500 status code, the application will redirect back to the main page.