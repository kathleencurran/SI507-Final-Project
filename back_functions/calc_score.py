def calc_tempo(tempo):
    new_tempo = 0
    if tempo < 70:
        new_tempo = 1
    elif 70 <= tempo < 80:
        new_tempo = 2
    elif 80 <= tempo < 90:
        new_tempo = 3
    elif 90 <= tempo < 100:
        new_tempo = 4
    elif 100 <= tempo < 110:
        new_tempo = 5
    elif 110 <= tempo < 120:
        new_tempo = 6
    elif 120 <= tempo < 130:
        new_tempo = 7
    elif 130 <= tempo < 140:
        new_tempo = 8
    elif 150 <= tempo < 160:
        new_tempo = 9
    else:
        new_tempo = 10

    return new_tempo * 10


def calc_acoustic(acoustic):
    acoustic_score = 0
    if acoustic < .2:
        acoustic_score = 10
    elif .2 <= acoustic <.4:
        acoustic_score = 8
    elif .4 <= acoustic < .5:
        acoustic_score = 6
    elif .5 <= acoustic < .6:
        acoustic_score = 4
    elif .6 <= acoustic < .8:
        acoustic_score = 2
    else:
        acoustic_score = 1
    return acoustic_score * 10

def calc_valence(valence):
    return int(valence * 100)

def calc_danceability(danceability):
    return int(danceability * 100)

def calc_energy(energy):
    return int(energy * 100)


