import pickle
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Movie Recommendation App")

def fetch_poster(movie_name):
    url = "http://www.omdbapi.com/?t={}&apikey=fa2c2e66".format(movie_name)
    data = requests.get(url)
    data = data.json()
    poster_path = data['Poster']
    return poster_path

def fetch_rating(movie_name):
    url = "http://www.omdbapi.com/?t={}&apikey=fa2c2e66".format(movie_name)
    data = requests.get(url)
    data = data.json()
    rating = data['imdbRating']
    return "".join(rating)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    
    recommended_movies = []
    recommended_posters = []
    recommend_rating = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].title))
        recommend_rating.append(fetch_rating(movies.iloc[i[0]].title))
    return recommended_movies,recommended_posters,recommend_rating
 

    
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# st.header('Movie Recommender System')
st.markdown("""<span style =" color : red; font-weight: bold; font-size: 49px;">Movie Recommender System</span>""", unsafe_allow_html=True)
st.markdown(
    """<span style ="font-size: 18px;
        font-weight: bold;
        color: #ff5c33; 
        font-family: 'Arial', sans-serif;
        margin-bottom: -20px; ">Select the Movie </span>""",
    unsafe_allow_html=True)
selected_movie_name =st.selectbox(
    "",
    movies['title'].values,
    label_visibility="collapsed"
)

#check if new value is selected
if selected_movie_name is not None:
    st.session_state.image_visible = True
        
# Initialize session state for image visibility
if ('image_visible' not in st.session_state):
    st.session_state.image_visible = True


def display_movie_grid(names, posters, ratings, items_per_row=3, image_width=210, image_height=340):
    for i in range(0, len(names), items_per_row):
        cols = st.columns(items_per_row)
        for idx, col in enumerate(cols):
            if i + idx < len(names):
                with col:
                    # Create HTML for the card
                     # Create HTML for the card
                    html_content = f"""
                    <div style="
                        display: flex;
                        flex-direction: column;
                        background-color:rgba(255, 255, 255, 0.1);
                        border: 2px white;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        padding: 10px;
                        text-align: center;
                        margin-bottom: 20px;
                        width: {image_width + 20}px;
                        height: 100%;
                    ">
                        <img src="{posters[i + idx]}" alt="{names[i + idx]}" style="
                            width:{image_width}px;
                            height:{image_height}px;
                            object-fit: cover;
                            border-radius: 10px;
                        ">
                        <div style="
                            background-color: red;
                            color: black;
                            font-weight: bold;
                            padding: 10px;
                            border-radius: 5px;
                            margin-top: 15px;
                            word-wrap: break-word;
                            overflow-wrap: break-word;
                            white-space: normal;
                            flex-grow: 1;
                            font-size: 14px;
                        ">
                            {names[i + idx]}
                            <br>
                            {"IMDB : "+ratings[i + idx]+"⭐"}
                        </div>
                    </div>
                    """
                    # Render the HTML
                    st.markdown(html_content, unsafe_allow_html=True)


# Function to toggle image visibility
def toggle_image():
    st.session_state.image_visible = not st.session_state.image_visible                   
                    
if st.button('Recommended'):
    hader =f""" <div style="
             background-color:rgba(255, 255, 255, 0.1);
             color: white;
             font-weight: bold;
             padding: 10px;
             border-radius: 5px;
             margin-top: 15px;
             word-wrap: break-word;
             overflow-wrap: break-word;
             white-space: normal;
             flex-grow: 1;
             font-size: 26px;
             width : 100%;
            ">
            {"Movie that are similer to "}
            <span style =" color : red; font-weight: bold; font-size: 26px;"> "{selected_movie_name}"</span>
            </div>
            <br>
            """
            # Render the HTML
    st.markdown(hader, unsafe_allow_html=True)
    toggle_image()
    recommended_movie_names, recommended_movie_posters, recommended_movie_ratings = recommend(selected_movie_name)
    display_movie_grid(recommended_movie_names, recommended_movie_posters, recommended_movie_ratings)
 
    
# Display the image based on visibility state
if st.session_state.image_visible:
    hader =f""" <div style="
             background-color:rgba(255, 255, 255, 0.1);
             color:rgba(255, 255, 255, 0.1);
             font-weight: bold;
             padding: 10px;
             border-radius: 5px;
             margin-top: 15px;
             margin-bottom: -15px;
             word-wrap: break-word;
             overflow-wrap: break-word;
             white-space: normal;
             flex-grow: 2;
             text-align: center;
             font-size: 35px;
             font-variant: small-caps;
             width : 100%;
             border: 1px solid red;
             text-shadow:
             -0.5px -0.5px 0 red, 
              0.5px -0.5px 0 red, 
             -0.5px  0.5px 0 red, 
              0.5px  0.5px 0 red;
            ">
            {"Find Your Next Movie Adventure"}
            </div>
            <br>
            """
            # Render the HTML
    st.markdown(hader, unsafe_allow_html=True)
    st.image('Movie_poster.jpg', use_container_width=True)

    # st.image('https://aml-group.com/app/uploads/2023/03/COLLAGE.jpg', use_container_width=True)

# Add custom CSS to style the social media icons row
st.markdown("""
    <style>
        .social-media-footer {
            background-color:rgba(255, 255, 255, 0.1);
            display: flex;
            justify-content: center;
            gap: 50px;
            padding: 5px;
            border-radius: 5px;
            margin-top: -10px;
            text-align: center;
            white-space: normal;
            flex-grow: 2;
            text-align: center;
            font-size: 23px;
            font-variant: small-caps;
            width : 100%;
            border: 1px solid red;
        }
        .social-media-footer a {
            text-decoration: none;
        }
        .social-media-footer img {
            width: 25px;
            height: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Add social media icons with hyperlinks (replace with actual URLs for your social media profiles)
st.markdown("""
    <div class="social-media-footer">
        <a href="https://www.facebook.com/rijwanool.karim?mibextid=ZbWKwL" target="_blank">
            <img src="https://cdn-icons-png.freepik.com/256/7448/7448197.png?semt=ais_hybrid" alt="Facebook">
        </a>
        <a href="https://www.linkedin.com/in/rijwanool-karim" target="_blank">
            <img src="https://cdn-icons-png.freepik.com/256/10091/10091641.png?semt=ais_hybrid" alt="Linkdin">
        </a>
        <a href="https://www.instagram.com/par_vez_04?igsh=MXNpOHUzN2R3dW9zaA==" target="_blank">
            <img src="https://cdn-icons-png.freepik.com/256/2504/2504918.png?ga=GA1.1.135314204.1736333148&semt=ais_hybrid" alt="Instagram">
        </a>
        <a href="https://x.com/Parvez__404?t=aRVw8DhrUZYV3pRQmyO5bw&s=09" target="_blank">
            <img src="https://cdn-icons-png.freepik.com/256/12452/12452435.png?ga=GA1.1.135314204.1736333148&semt=ais_hybrid" alt="Twitter">
        </a>
        <a href="https://github.com/A3x-parvez" target="_blank">
            <img src="https://cdn-icons-png.freepik.com/256/10090/10090288.png?ga=GA1.1.135314204.1736333148&semt=ais_hybrid" alt="GitHub">
        </a>
    </div>
        <p style =" color : white; font-weight: normal; font-size: 12px;  font-style: italic;  justify-content: center; text-align: center;"> &copy; Developed by parvez </p>
""", unsafe_allow_html=True)
