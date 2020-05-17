import requests
import streamlit as st
import json

st.title('spotify analysis yeah')
playlist_uri = 'spotify:playlist:1RvBa3Bfsso7UgiMrgEyH5'
id_from_spotify_uri = lambda uri: uri.split(':')[-1]
playlist_id = id_from_spotify_uri(playlist_uri)

with open('secrets.json', 'r') as f:
    secrets = json.loads(f.read())
    if 'token' not in secrets:
        raise Exception('secrets.json needs a token field')

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {secrets['token']}"
}


def get_tracks(playlist_id):
    get_track_id = lambda item: item['track']['id']
    get_first_artist = lambda item: item['track']['artists'][0]['name']
    get_track_title = lambda item: item['track']['name']
    get_track_duration = lambda item: item['track']['duration_ms']
    get_first_artist_id = lambda item: item['track']['artists'][0]['id']
    artist_genre_cache = {}

    request_uri = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    resp = requests.get(request_uri, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"something went wrong, here's the response\n{resp.text}")
    resp_data = resp.json()

    return [{
        'id':
        get_track_id(track),
        'artist':
        get_first_artist(track),
        'title':
        get_track_title(track),
        'durationMs':
        get_track_duration(track),
        'genres':
        get_artist_genres(get_first_artist_id(track), artist_genre_cache)
    } for track in resp_data['items']]


def get_track_features(track_id):
    features_i_care_about = ['energy', 'tempo', 'valence', 'danceability']

    request_uri = f"https://api.spotify.com/v1/audio-features/{track_id}"
    resp = requests.get(request_uri, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"something went wrong, here's the response\n{resp.text}")
    resp_data = resp.json()

    return {feature: resp_data[feature] for feature in features_i_care_about}


def get_artist_genres(artist_id, cache={}):
    request_uri = f"https://api.spotify.com/v1/artists/{artist_id}"
    if artist_id not in cache:
        resp = requests.get(request_uri, headers=headers)
        if resp.status_code != 200:
            raise Exception(
                f"something went wrong, here's the response\n{resp.text}")
        resp_data = resp.json()
        genres = resp_data['genres']
        cache[artist_id] = genres
        return genres
    else:
        st.write(f'cache hit with {artist_id}')
        return cache[artist_id]


data = [{
    **track, 'features': get_track_features(track['id'])
} for track in get_tracks(playlist_id)]

st.write(data)

with open('spotify.json', 'w') as f:
    f.write(json.dumps(data, indent=2))
    st.write('done writing to spotify.json')
    st.balloons()
