import sys
sys.path.append("..")
sys.path.append("../utils")

from parse_dict import *
from ru_soundex.soundex import RussianSoundex
from ru_soundex.distance import SoundexDistance


def sound_preprocessing_not_dict(path, POS = None):
    soundex = RussianSoundex(delete_first_letter=True)
    soundex_distance = SoundexDistance(soundex)
    words = open(path, 'r')
    for slot in words:
        x, y = slot.split()
        dist = soundex_distance.distance(x, y)
        if POS:
            print(POS, x, y, dist)
        else:
            print(x, y, dist)

def sound_preprocessing(path, part=0):
    soundex = RussianSoundex(delete_first_letter=True)
    soundex_distance = SoundexDistance(soundex)
    red = parse_dict(path)
    for slot in red:
        part_of_speech, words = slot
        if part != 0 and part_of_speech != part:
            continue
        for w1 in range(len(words)):
            for w2 in range(w1+1, len(words)):
                x = words[w1]
                y = words[w2]
                dist = soundex_distance.distance(x, y)
                print(x, y, dist)

def soundex_transform(file):
    soundex = RussianSoundex(delete_first_letter=True)
    d = SoundexDistance(soundex)
    f = open(file, 'r')

    for line in f:
        _, a, b = line.strip().split()
        print(a, b, soundex.transform(a.lower()), soundex.transform(b.lower()), d.distance(a.lower(), b.lower()))

    f.close()

def main():
    use_dict = True
    transform = True
    if transform:
        soundex_transform(sys.argv[1])

    if use_dict:
        sound_preprocessing(sys.argv[1], int(sys.argv[2]))
    else:
        sound_preprocessing_not_dict(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
    main()
