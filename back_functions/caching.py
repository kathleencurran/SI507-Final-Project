import json
from json import JSONEncoder
import os

'''https://pynative.com/make-python-class-json-serializable/'''
class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def open_cache(cache_filename):
    try:
        cache_file = open(cache_filename, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict


def save_cache(cache_dict, cache_filename):
    dumped_json_cache = json.dumps(cache_dict, indent=4, cls=DataEncoder)
    fw = open(cache_filename,"w")
    fw.write(dumped_json_cache)
    fw.close()


def store_cache_data(song_obj, cache_filename):
    n_key = str(song_obj.id)
    print('\ncaching', n_key)
    if n_key in SONG_CACHE:
        print('key in cache already')
        print(SONG_CACHE[n_key])
        return SONG_CACHE[n_key]
    else:
        print('looks like a new song \n')
        SONG_CACHE[n_key] = song_obj

        save_cache(SONG_CACHE, cache_filename)
        print('returning', type(SONG_CACHE[n_key]))
        return SONG_CACHE[n_key]

SONG_CACHE = open_cache('song_data.json')

def clear_cache(cache_filename):
    # for testing purposes, clearing tree of unnecessary data
    os.remove(cache_filename)

