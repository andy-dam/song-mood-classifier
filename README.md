# Song Mood Classifier

A ML model that predicts based on a song's audio features its mood from 4 options: Happy, Sad, Calm, and Energetic

## Description

This model is built using the Random Forest Classifier from the Scikit-Learn library. Other models that were tested included K-Nearest Neighbors and Support Vector Machine, but RFC gave the highest accuracy. A simple frontend was built using Flask for easy use of the model. To get the audio features of the song, the app uses the Spotify Web API to query the song and receive results. The criteria used for classifying are:

1. Danceability: Describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
2. Energy: A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
3. Loudness: The overall loudness of a track in decibels (dB). (Averaged across the entire track)
4. Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value.
5. Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
6. Instrumentalness: Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
7. Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. 
8. Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
9. Tempo: The overall estimated tempo of a track in beats per minute (BPM).
(These descriptions are from the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/reference/get-audio-features))

## Getting Started

### Dependencies
The Flask app was built using these versions of these libraries:

* Python 3.12.5
* Flask 3.0.3
* Spotipy 2.24.0
* Joblib 1.4.2

### Installing
To run this app, run these commands:
```
pip install flask==3.0.3
pip install spotipy==2.24.0
pip install joblib==1.4.2
```

### Executing program
In order to run this program, you must have your own Spotify Web API Client ID and Client Secret keys as environment variables on your system. To add environment variables to Windows, press the WIN key and search "Edit the system environment variables", and after pressing the "Environment Variables...", add new environment variables named "SPOTIFY_CLIENT_ID" and "SPOTIFY_CLIENT_SECRET" with their values equal to their respective keys. To get the Spotify keys, head to the [developer page](https://developer.spotify.com/) and login with your Spotify account. After signing in, go to the Dashboard and create an app using the Web API. Once created, go to the Settings of the app and copy the client id and secret.

To run the program, run the app.py file:
```
python app.py
```

## Authors

Andy Dam 
[@andy-dam](https://www.github.com/andy-dam/)


## Acknowledgments

The app uses the [278k Emotion Labeled Spotify Songs](https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset) dataset from Kaggle which is under the [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.
