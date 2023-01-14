import openpyxl
import xlrd, xlwt
import re
import os
import sys
sys.path.append("..")
sys.path.append("../utils")

from api import *
from parse_dict import *

def get_distant(model,filepath, ps=0):
    #for excel files
    #doing workbooks
    tmp_tag = {
        1: '_NOUN',
        2: '_VERB',
        3: '_ADJ',
        4 :'_ADV'
    }

    parsed = open(filepath, 'r')

    #cycle for pairs of words
    for line in parsed:
        pair = line.strip().split()
        if int(pair[2]) < 7:
            continue
        k = api_similarity(model, pair[0] + tmp_tag[ps], pair[1]+tmp_tag[ps])
        if 'nknown'not in k:
            k = float(k)
            print(ps, pair[0], pair[1], pair[2], str(k))

#-----------------------------------------------------------------
#------------Utils------------------------------------------------
#-----------------------------------------------------------------

def delete_symbols(word, kind='word'):
    if kind == 'word':
        new = ''
    #    print(word)
        for c in word:
            if c not in ('*','-','+','1','2','3','4','5','6'):
                new = new +  c
    elif kind == 'morph':
        new = Morph(word)
    return new

def print_pairs(pairs):
    p = pairs
    for i in range(len(pairs)):
        t = pairs[i]
        for j in range(len(t[1])):
            st = t[0] + '-'  + t[1][j]
            print(st)
def put_pairs(pairs):
    p = pairs
    for i in range(len(pairs)):
        t = pairs[i]
        for j in range(len(t[1])):
            st = t[0] + '-' + t[1][j]
            print(st)

def count(file):
    pairs = parse_dict(file)
    counter = 0
    print(len(pairs))
    for i in range(len(pairs)):
        t = pairs[i][1]
        counter += len(t) * (len(t)-1)
    return counter

def main():
    PART_OF_SPEECH = 3
    models = [ 'tayga_upos_skipgram_300_2_2019',
               'ruscorpora_upos_cbow_300_20_2019',
               #'ruwikiruscorpora_upos_skipgram_300_2_2019',
               #'tayga_none_fasttextcbow_300_10_2019',
               #'news_upos_skipgram_300_5_2019',
               #'araneum_none_fasttextcbow_300_5_2018'
             ]
    filepath = sys.argv[1]
    for i in range(len(models)):
        get_distant(models[i], filepath, PART_OF_SPEECH)
if __name__ == "__main__":
    main()

