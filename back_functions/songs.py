
from back_functions import secret, calc_score, caching


import requests


client_key = secret.CLIENT_ID
client_secret = secret.CLIENT_SECRET
access_token = secret.ACCESS_TOKEN


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
rules ='&market=US&limit=1'

mood = {
    'club': list(range(80, 101)),
    'party': list(range(60, 80)),
    'car': list(range(40, 60)),
    'kickback': list(range(20, 40)),
    'quiet': list(range(0, 20))
}

class Song:
    def __init__(self, id = '', name='', artist='', attributes = [], score=50.00, vibe=''):
        self.id = id
        self.name = name
        self.artist = artist
        self.attributes = attributes
        self.score = score
        self.vibe = vibe

    def create_song_obj(self, id):
        song = requests.get(BASE_URL + 'tracks/' + id, headers=headers)
        song = song.json()

        try:
            song_artist = song['artists'][0]['name']
            song_name = song['name']

            self.id = id
            self.name = song_name
            self.artist = song_artist
            self.attributes = self.get_audio_feats()
            self.score = self.score_song()
            self.vibe = self.determine_song_vibe()

            song_obj = Song(self.id, self.name, self.artist, self.attributes, self.score, self.vibe)

            print('we\'re making it to create song')

            return song_obj
        except:
            print('CREATING - null track')



    def find_song_id(self):
        result = requests.get(BASE_URL + 'search?q={track}%{artist}&type=track'
                              .format(track=self.name, artist=self.artist) +
                              rules,
                              headers=headers)
        result = result.json()
        try:
            self.id = result['tracks']['items'][0]['id']
            return self.id
        except:
            print('SONG ID - null track')


    def get_audio_feats(self):
        result = requests.get(BASE_URL +
                              'audio-features/{id}'.format(id=self.id),
                              headers=headers)
        result = result.json()

        try:
            arr = [result['danceability'],
                   result['energy'],
                   result['valence'],
                   result['acousticness'],
                   result['tempo']]

            danceability_score = calc_score.calc_danceability(result['danceability'])
            energy_score = calc_score.calc_energy(result['energy'])
            valence = calc_score.calc_valence(result['valence'])
            tempo_score = calc_score.calc_tempo(result['tempo'])
            acoustic_score = calc_score.calc_acoustic(result['acousticness'])

            self.attributes = [danceability_score, energy_score, valence, acoustic_score, tempo_score]
            return self.attributes

        except:
            print('AUDIO FEATS - null track')


    def score_song(self):
        total = 0
        try:
            for i in self.attributes:
                total += i

            song_score = total/len(self.attributes)
            self.score = round(song_score, 2)
            return self.score
        except:
            print('SCORE - null track')

    def determine_song_vibe(self):
        try:
            if self.score >= 80:
                self.vibe = 'Party'
                return self.vibe
            elif 55 <= self.score < 80:
                self.vibe = 'Car Jams'
                return self.vibe
            elif 40 <= self.score < 55:
                self.vibe = 'Kickback'
                return self.vibe
            elif 1 <= self.score < 40:
                self.vibe = 'Quiet'
                return self.vibe
            else:
                return self.vibe
        except:
            print('SONG VIBE - null track')

