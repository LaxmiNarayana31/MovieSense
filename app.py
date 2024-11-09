import pickle
import streamlit as st
import requests
from imdb import IMDb
from dotenv import load_dotenv
import os

# Initialize IMDb instance
ia = IMDb()

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

try:
    movies = pickle.load(open('model/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))
except (FileNotFoundError, IOError) as e:
    st.error(f"Error loading data files: {e}")
    st.stop()

# Fetch IMDb rating using IMDbPY
def fetch_imdb_rating(movie_title):
    try:
        search_results = ia.search_movie(movie_title)
        if search_results:
            movie = ia.get_movie(search_results[0].movieID)
            return movie.get('rating')
    except Exception as e:
        print(f"Error fetching IMDb rating for {movie_title}: {e}")
    return None

# Fetch movie poster
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w300/{poster_path}" if poster_path else None
    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
    return None

# Fetch short movie reviews
def fetch_reviews(movie_id, max_length=200):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        reviews_data = response.json().get('results', [])
        
        short_reviews = []
        for review in reviews_data[:3]:  # Get only first 3 reviews
            review_text = review['content']
            if len(review_text) > max_length:
                review_text = review_text[:max_length] + '...'
            short_reviews.append(review_text)
        return short_reviews
    except Exception as e:
        print(f"Error fetching reviews for movie ID {movie_id}: {e}")
    return ["No reviews available."]

# Fetch trailer
def fetch_trailer(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        for video in response.json().get('results', []):
            if video['type'] == 'Trailer':
                return f"https://www.youtube.com/embed/{video['key']}"
    except Exception as e:
        print(f"Error fetching trailer for movie ID {movie_id}: {e}")
    return None

# Recommendation function
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_reviews = []
        recommended_movie_trailers = []
        recommended_movie_ratings = []
        
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            title = movies.iloc[i[0]].title
            recommended_movie_names.append(title)
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_reviews.append(fetch_reviews(movie_id))
            recommended_movie_trailers.append(fetch_trailer(movie_id))
            recommended_movie_ratings.append(fetch_imdb_rating(title))

        return recommended_movie_names, recommended_movie_posters, recommended_movie_reviews, recommended_movie_trailers, recommended_movie_ratings
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return [], [], [], [], []

# Streamlit UI
st.header('Movie Recommender System')

# Select movie from the list
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_reviews, recommended_movie_trailers, recommended_movie_ratings = recommend(selected_movie)
    
    for i in range(5):
        st.subheader(recommended_movie_names[i])
        
        # Display movie details with aligned layout
        with st.container():
            poster_col, trailer_col = st.columns([1, 1.5])

            with poster_col:
                if recommended_movie_posters[i]:
                    st.image(recommended_movie_posters[i], width=150)
                else:
                    st.write("Poster not available")

            with trailer_col:
                trailer_url = recommended_movie_trailers[i]
                if trailer_url:
                    st.write("Trailer:")
                    st.markdown(
                        f'<iframe width="320" height="180" src="{trailer_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                        unsafe_allow_html=True
                    )
                else:
                    st.write("Trailer not available")

            st.write(f"**IMDb Rating:** {recommended_movie_ratings[i]}/10" if recommended_movie_ratings[i] else "Rating not available")

            st.write("Reviews:")
            reviews = recommended_movie_reviews[i]
            for review in reviews:
                st.write(f"- {review}")
