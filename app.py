from turtle import width
from urllib import response
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    # Access Key: 45865cf8574fd4d67ca334db8febbbbb
    access_token = '45865cf8574fd4d67ca334db8febbbbb'

    URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={access_token}'

    response = requests.get(URL)
    data = response.json()
    poster_path = data['poster_path']
    base_url = 'https://image.tmdb.org/t/p/w500'
    full_poster_path = base_url + poster_path

    return full_poster_path


def recommend(movies_list, similarity, movie):
    movie_index = movies_list[movies_list['title']
                              == selected_movie_name].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    posters = []

    for m in movie_list[1:6]:
        movie_id = movies_list.iloc[m[0]].movie_id
        recommended_movies.append(movies_list.iloc[m[0]].title)
        posters.append(fetch_poster(movie_id))

    return recommended_movies, posters


if __name__ == '__main__':
    # Import the pickle files
    movies_list_pickle = pickle.load(open('movies.pkl', 'rb'))
    movies_list = pd.DataFrame(movies_list_pickle)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # Start the Design
    st.set_page_config(page_title='MRS', page_icon=None, layout="centered",
                       initial_sidebar_state="auto", menu_items=None)

    st.title('Movie Recommendation System')

    # Select the Movie
    selected_movie_name = st.selectbox(
        'How would you like to watch?',
        movies_list['title'].values
    )

    # Button Click Events
    if st.button('Recommend'):
        movies_name, movies_poster = recommend(
            movies_list, similarity, selected_movie_name)

        # Columns for numbers of movie card in each line
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(movies_name[0])
            st.image(movies_poster[0])

        with col2:
            st.text(movies_name[1])
            st.image(movies_poster[1])

        with col3:
            st.text(movies_name[2])
            st.image(movies_poster[2])

        with col4:
            st.text(movies_name[3])
            st.image(movies_poster[3])

        with col5:
            st.text(movies_name[4])
            st.image(movies_poster[4])
