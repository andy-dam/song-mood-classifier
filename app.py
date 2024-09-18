''' Import libraries '''
from flask import Flask, render_template, url_for, request
import joblib
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

''' Initialize the Flask app '''
app = Flask(__name__)


''' Initialize the Spotify API '''
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))


''' Load the model and scaler '''
model = joblib.load('rfc.joblib')
scaler = joblib.load('scaler.joblib')


''' 
This function will search for the song on Spotify, extract its features, 
scale the features and predict the genre of the song

Args:
    song_name (str): The name of the song to predict
    
Returns:
    str: The predicted genre of the song
    str: The name of the artist of the song
    str: The url of the album cover of the song
'''
def predict_song(song_name):
    song = None
    while song is None:
        try:
            song = sp.search(q=song_name, limit=1)
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error occurred: {e}. Retrying...")
    song_id = song['tracks']['items'][0]['id']
    song_features = sp.audio_features(song_id)[0]
    X = [song_features['danceability'], song_features['energy'], song_features['loudness'], 
            song_features['speechiness'], song_features['acousticness'], song_features['instrumentalness'], 
            song_features['liveness'], song_features['valence'], song_features['tempo']]

    X = scaler.transform([X])[0]
    prediction = model.predict([X])[0]
    
    artist = song['tracks']['items'][0]['artists'][0]['name']
    album_cover = song['tracks']['items'][0]['album']['images'][1]['url']
    song_name = song['tracks']['items'][0]['name']
    
    return prediction, song_name, artist, album_cover


'''Home route'''
@app.route('/')
def index():
    return render_template('index.html')

'''Predict route'''
@app.route('/predict', methods=['POST'])
def predict():
    song_name = request.form['song_name']
    mood, song_name, artist, album_cover = predict_song(song_name)
    # make mood capitalized
    mood = mood.capitalize()
    return render_template('index.html', mood=mood, artist=artist, album_cover=album_cover, song_name=song_name)


'''About route'''
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)