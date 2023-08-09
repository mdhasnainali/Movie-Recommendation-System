# Movie Recommendation System

This is a content-based recommendation system for movies.

## Introduction

This project implements a movie recommendation system using a content-based approach. The system suggests similar movies based on the content of the movies, including their genres, keywords, cast, crew, and overview.

## View

![View]('./gif/view.gif)

## Dependencies

Make sure you have the following dependencies installed:

- numpy
- pandas
- scikit-learn
- nltk
- streamlit

You can install these dependencies using the following command:

```bash
pip install numpy pandas scikit-learn nltk streamlit
```

## Dataset

The dataset used for this project is the "TMDB 5000 Movie Dataset," containing information about movies' attributes such as title, overview, genres, keywords, cast, and crew. The dataset can be found at [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mdhasnainali/Movie-Recommendation-System.git
cd movie-recommendation-system
```
2. Run the Streamlit app:

3. Run the notebook

```bash
streamlit run app.py
```

4. Open a web browser and navigate to `http://localhost:8501` to interact with the movie recommendation system.

## How It Works

- The dataset is processed to extract relevant features such as genres, keywords, cast, crew, and overview.
- Text preprocessing techniques are applied, including stemming and lowercase conversion.
- A CountVectorizer is used to transform the textual data into a numerical format suitable for machine learning.
- Cosine similarity is calculated between movie vectors to measure their similarity.
- Given a movie, the system recommends similar movies based on their content.

## Files

- `app.py`: The Streamlit web application for interacting with the recommendation system.
- `dataset/tmdb_5000_movies.csv`: The movie dataset.
- `dataset/tmdb_5000_credits.csv`: The credits dataset.

## Results

The recommendation system provides suggestions for similar movies based on the content of the input movie. The output includes the top recommended movies for each input movie.

## Acknowledgments

- The dataset used in this project is sourced from [TMDB](https://www.themoviedb.org/).
- This project is for educational purposes and showcases a simple content-based recommendation system.

## License

This project is licensed under the [MIT License](LICENSE).
