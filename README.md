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
 

# Setting up the Project

1. Clone the repository using the command `git clone https://github.com/LaxmiNarayana31/MovieSense.git`
2. Create a virtual environment using `pipenv shell`
3. Install the required packages using `pipenv install` (make sure you have pipenv installed in your machine)
4. Create a `.env` file and add the TMDB API key to it.
5. Run the script using `streamlit run app.py` or `pipenv run app`
