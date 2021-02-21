import sys
from ..parse_dict import *
from ru_soundex.soundex import RussianSoundex
from ru_soundex.distance import SoundexDistance


def sound_preprocessing_not_dict(path):
    soundex = RussianSoundex(delete_first_letter=True)
    soundex_distance = SoundexDistance(soundex)
    words = open(path, 'r')
    for slot in words:
        x, y = slot.split()
        dist = soundex_distance.distance(x, y)
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
                x = words[w1][2]
                y = words[w2][2]
                dist = soundex_distance.distance(x, y)
                print(x, y, dist)

def main():
    use_dict = False
    if use_dict:
        sound_preprocessing(sys.argv[1], int(sys.argv[2]))
    else:
        sound_preprocessing_not_dict(sys.argv[1])

if __name__ == "__main__":
    main()
