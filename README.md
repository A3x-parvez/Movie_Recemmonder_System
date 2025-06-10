# Movie Recommender System

`Movie Recommender System is a Streamlit application that suggests movies to users based on their preferences. By leveraging machine learning techniques, this system analyzes movie data to provide personalized recommendations tailored to individual tastes.`

---

## 🚀 Live Demo

Try the Movie Recommender System live at: [Live Demo](https://movies-recommendation-parvez.streamlit.app/)

---

## 📖 Overview

**Movie Recommender System** is an interactive web application built using **Streamlit** that provides movie suggestions based on a selected movie. It uses **content-based filtering** and machine learning techniques to recommend the most similar movies from a dataset of over 5000 films.

The system is trained on the **TMDb 5000 Movie Dataset**, which includes metadata like genres, cast, crew, and plot overviews. During preprocessing, the dataset is cleaned, merged, and transformed using techniques such as:

- 🧹 **Data Preprocessing**: Merging movie metadata and credits, removing duplicates, and creating a combined feature (tags).
- 🧠 **Feature Extraction**: Text vectorization using `CountVectorizer` to convert textual data into numerical form.
- 📏 **Similarity Measurement**: Calculating **cosine similarity** between movies to find how closely related they are based on metadata.

### 🔍 How It Works:
1. A user selects a movie from the dropdown list.
2. The app uses the **cosine similarity matrix** to find the top **6 most similar movies**.
3. The **TMDb API** is used to fetch poster images of the recommended movies.
4. The recommended movies are displayed using a clean and responsive **Streamlit UI**.

This project combines **data processing**, **machine learning**, and **user interface design** to deliver a fast, simple, and engaging movie recommendation experience.

---

## ✨ Features

- 🎬 **User  -Friendly Interface**: An intuitive interface for seamless user interaction.
- 🤖 **Machine Learning Algorithms**: Implements various algorithms to analyze movie similarities and user preferences.
- 📥 **Data Storage**: Efficiently stores movie data and similarity matrices using pickle files.
- 🔄 **Customizable**: Easily modify the dataset and algorithms to fit your needs.

---


## 🛠️ Setup and Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/A3x-parvez/Movie_Recemmonder_System.git
    cd Movie_Recemmonder_System
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🎬 Usage

1. **Run the Streamlit Application:**
    ```bash
    streamlit run app2.py
    ```
    The app will be available at [http://127.0.0.1:8501](http://127.0.0.1:8501).

2. **Input Preferences:** Select the movie from the dropdown menu and click Recommended button.

3. **Receive Recommendations:** View 6 personalized movie recommendations based on your input.

---

## 📁 Project Structure
```
Movie_Recommender_System/
│
├── Movies_Recommender_system_ML_Code/ # Jupyter notebooks with ML training code
│      │            
│      ├── movie_dict.pkl                      # Pickle file storing dictionary of movie titles and metadata
│      ├── movies.pkl                          # Pickle file with cleaned movie DataFrame for app
│      ├── similarity.pkl                      # Precomputed similarity matrix (cosine similarity)
│      │
│      ├── tmdb_5000_movies.csv                # Original TMDb dataset (movie metadata)
│      ├── tmdb_5000_credits.csv               # Original TMDb dataset (cast, crew, credits)
│      │
│      └── movie_recommended_system.ipynb      # Main Jupyter notebook used for building and training the model
│
│
├── venv/ # Python virtual environment (do not track)
│
├── app2.py # Main application script (Flask or Streamlit)
├── movie_dict.pkl # Dictionary of movies used for UI display
├── movies.pkl # Movie metadata used for recommendation
├── similarity.pkl # Precomputed cosine similarity matrix
├── Movie_poster.jpg # Thumbnail/preview image
├── requirments.txt # List of dependencies
├── README.md # Project documentation
└── .gitattributes # Git metadata

```
---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

---

## 🌐 Social Media

Connect with me on:  

[![GitHub](https://img.shields.io/badge/GitHub-@A3x--parvez-181717?style=flat&logo=github)](https://github.com/A3x-parvez)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rijwanool_karim-blue?style=flat&logo=linkedin)](https://linkedin.com/in/rijwanool-karim/)  

---

## 📧 Contact / Support

If you have any questions or want to get in touch:

- GitHub : [A3x-parvez](https://github.com/A3x-parvez)  
- Email : rijwanoolkarim143r@gmail.com

---
