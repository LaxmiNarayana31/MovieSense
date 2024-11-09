# Setting up the Project

1. Clone the repository using the command `git clone https://github.com/LaxmiNarayana31/MovieSense.git`
2. Create a virtual environment using `pipenv shell`
3. Install the required packages using `pipenv install` (make sure you have pipenv installed in your machine)
4. Create a `.env` file and add the TMDB API key to it.
5. Run the script using `streamlit run app.py` or `pipenv run app`

# What is this project?

This project is a content-based movie recommender system using cosine similarity. It takes a movie title as input and recommends five movies that are similar to the input movie. The movies are fetched from the TMDB API and the similarity is calculated using cosine similarity. The project also fetches the movie poster, reviews, and trailer for the recommended movies. The project uses Streamlit for the user interface and the IMDb API for fetching movie ratings. 

The dataset used for this project is from [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
