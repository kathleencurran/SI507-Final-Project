from flask import Flask, render_template, request

import sys
sys.path.append('/Users/kathleencurran/Documents/SI507/Final/pythonProject')
from back_functions import playlist, secret, dictionary, tree


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('spotify_form.html')

global_file = 'song_data.json'

@app.route('/handle_form', methods=['POST'])
def handle_the_form():

    vibe = request.form["vibe"]
    url = request.form["playlist-url"]

    quiet = dictionary.get_def_of_all()[0]
    kickback = dictionary.get_def_of_all()[1]
    car_jam = dictionary.get_def_of_all()[2]
    party = dictionary.get_def_of_all()[3]
    upper = 100
    lower = 0

    if vibe == 'Quiet':
        upper, lower = 39, 1
    elif vibe == 'Kickback':
        upper, lower = 54, 40
    elif vibe == 'Car Jams':
        upper, lower = 79, 55
    elif vibe == 'Party':
        upper, lower = 100, 80
    else:
        print('oops something went wrong')

    try:
        pl_url = playlist.url_parser(url)
        pl = playlist.Playlist(pl_url).retrieve_from_id()
        print(pl)
        print(pl == True)

        length = len(pl.playlist_tracks)

        print('caching')
        pl.cache_all_songs()

        tree_pl = tree.BinarySearchTree()

        print(global_file)
        tree_pl.create_tree_from_cache(global_file)
        print(type(tree_pl))

        recommendation = tree_pl.access_and_recommend(global_file, lower, upper)

        return render_template('playlist_result.html',
                               vibe=vibe,
                               playlistName=pl.title,
                               scoredVibe=pl.vibe,
                               score=pl.score,
                               quiet_def=quiet,
                               kickback_def=kickback,
                               car_jam_def=car_jam,
                               party_def=party,
                               length=length,
                               recommendation=recommendation)

    except:
        print('oops, something is wrong with your url. Please try again')

@app.route('/')
def try_again():
    render_template('spotify_form.html')

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)