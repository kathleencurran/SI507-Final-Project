import requests

from back_functions import songs, secret, tree, caching


client_key = secret.CLIENT_ID
client_secret = secret.CLIENT_SECRET
access_token = secret.ACCESS_TOKEN

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

class Playlist:
    def __init__(self, id, title='', playlist_tracks = [], score = 0.0, vibe = ''):
        self.id = id
        self.title = title
        self.playlist_tracks = playlist_tracks
        self.score = score
        self.vibe = vibe

    def retrieve_from_id(self):
        '''
            takes the ID of the playlist, retrieves its info from the api
            and then creates a list of Song Objects as its attributes
        '''

        playlist = requests.get(BASE_URL + 'playlists/' + self.id, headers=headers)
        playlist = playlist.json()

        tracks = playlist['tracks']['items']
        playlist_len = len(tracks)

        song = songs.Song()

        id_list = [tracks[i]['track']['id'] for i in range(0, playlist_len)]
        song_list = [song.create_song_obj(i) for i in id_list]

        self.playlist_tracks = song_list
        self.score = self.calc_playlist_score()
        self.title = playlist["name"]
        self.vibe = self.determine_song_vibe()
        print('we made it to retrieve from id')
        pl_obj = Playlist(self.id, self.title, self.playlist_tracks, self.score, self.vibe)

        print(pl_obj.__dict__)
        return pl_obj


    def cache_all_songs(self):
        for songs in self.playlist_tracks:
            caching.store_cache_data(songs, 'song_data.json')


    def calc_playlist_score(self):
        try:
            num_items = len(self.playlist_tracks)
            score_sum = 0
            for items in self.playlist_tracks:
                score_sum += items.score
            return round((score_sum/num_items), 2)
        except:
            print('null track')

    def determine_song_vibe(self):
        print('SCORE',self.score)
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


    def create_or_add_tree(self, some_tree):
        for items in self.playlist_tracks:
            some_tree.put(items.score, items)
        return some_tree


def url_parser(playlist_url):
    url = playlist_url.split("/")
    last_bit = url[-1]
    id = last_bit.split("?")
    return id[0]

