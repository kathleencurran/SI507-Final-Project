import requests
import json

app_id = '66c73e4d'
app_key = 'd802904c14d9a9feff43ad3b23d01d08'
language = 'en-gb'
word_id = 'quiet'

word_list = ['quiet', 'hang out', 'sing-along', 'banger']

def get_definition(id):

    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'.format(word=id)

    response = requests.get(url)
    response = response.json()
    def_list = response[0]['meanings'][0]['definitions']
    return def_list


def get_def_of_all(a_list=[]):
    quiet = get_definition(word_list[0])
    quiet_def = quiet[0]['definition']
    a_list.append(quiet_def)

    hangout = get_definition(word_list[1])
    hangout_def = hangout[2]['definition']
    a_list.append(hangout_def)

    car_bop = get_definition(word_list[2])
    bop_def = car_bop[0]['definition']
    a_list.append(bop_def)

    party = get_definition(word_list[3])
    party_def = party[3]['definition']
    a_list.append(party_def)

    return a_list



