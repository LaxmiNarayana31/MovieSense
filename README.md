# Project Overview

- **Content-based Movie Recommender**: The project is a content-based movie recommendation system.
- **Input**: Takes a movie title as input from the user.
- **Recommendation**: Recommends five movies that are similar to the input movie based on cosine similarity.
- **TMDB API**: Fetches movie data (e.g., title, genre, plot) using the TMDB API.
- **Cosine Similarity**: Calculates similarity between movies using cosine similarity.
- **Movie Details**: Retrieves additional information about the recommended movies, such as:
  - Movie posters
  - Reviews
  - Trailers
- **User Interface**: Built with Streamlit for an interactive, easy-to-use UI.
- **IMDb API**: Integrates IMDb API to fetch movie ratings for the recommended movies.
- **Dataset**: The project uses a dataset available from [kaggle.](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Project Setup

- Clone the repository:
  ```bash
  git clone https://github.com/LaxmiNarayana31/MovieSense.git
  ```
- Create a virtual environment using pipenv. If you don't have pipenv installed, you can install it by running `pip install pipenv` in your terminal.
  ```bash
  pipenv shell # Create a virtual environment
  pipenv install # Install dependencies
  ```
- Create a `.env` file and add the TMDB API key to it.

  ```bash
  TMDB_API_KEY=
  ```

- Run the application:
  ```bash
  pipenv run main
  ```
  or
  ```bash
  streamlit run main.py
  ```
