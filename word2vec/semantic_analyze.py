import openpyxl
import xlrd, xlwt
import re
import os
import sys
sys.path.append("..")
sys.path.append("../utils")

from api import *
from parse_dict import *

def get_distant(model, direct, filepath, form='csv', find_n=False, ps=0):
    #for excel files
    #doing workbooks
    tmp_tag = {
        1: '_NOUN',
        2: '_VERB',
        3: '_ADJ',
        4 :'_ADV'
    }
    unknown_words = { i:0 for i in range(1, 5)}

    tmp = [xlwt.Workbook() for i in range(5)]
    files = [tmp[i].add_sheet('Word_{:d}'.format(i)) for i in range(5)]
    curr = [0 for i in range(5)]
    parsed = parse_dict(filepath, kind='word')
    os.makedirs(direct)

    #cycle for pairs of words
    for i in range(len(parsed)):
        t = parsed[i]
        pairs = t[1]
        cl = 0
        if ps and t[0] != ps:
            continue
        for j in range(len(pairs)):
            for p in range(j+1, len(pairs)):
                #print(pairs[j], pairs[p])
                k = api_similarity(model, pairs[j] + tmp_tag[t[0]], pairs[p]+tmp_tag[t[0]])
                if 'nknown'not in k:
                    k = float(k)
                    if find_n:
                        z = search_word(model,pairs[j] + tmp_tag[t[0]], pairs[p] + tmp_tag[t[0]], form)
                        other_z = search_word(model,pairs[p] + tmp_tag[t[0]], pairs[j] + tmp_tag[t[0]], form) 
                        #z = search_word(model,pairs[j] + tmp_tag[t[0]], pairs[p], form)
                        #other_z = search_word(model,pairs[p] + tmp_tag[t[0]], pairs[j], form)

                    if k >= 0.9:
                        print(pairs[j], pairs[p])
                        files[t[0]-1].write(curr[t[0]-1], 0, pairs[j])
                        files[t[0]-1].write(curr[t[0]-1], 1, pairs[p])
                        files[t[0]-1].write(curr[t[0]-1], 2, k)
                    #if find_n and z == 'Yes' and other_z == 'Yes':
                    #    files[t[0]-1].write(curr[t[0]-1], 3, z)
                        cl += 1
                        curr[t[0]-1] += 1
                else:
                    unknown_words[t[0]] += 1
                    files[4].write(curr[4], 0, pairs[j])
                    files[4].write(curr[4], 1, pairs[p])
                    curr[4] += 1

    print("Total number of pairs: ", cl)
    for p in range(5):
        tmp[p].save(os.path.join(direct, 'results_{:d}.xls'.format(p)))

    print(model, unknown_words)

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
    PART_OF_SPEECH = 0
    FIND_NEIGHBOUR = False
    models = [ 'tayga_upos_skipgram_300_2_2019',
               'ruscorpora_upos_cbow_300_20_2019',
               #'ruwikiruscorpora_upos_skipgram_300_2_2019',
               #'tayga_none_fasttextcbow_300_10_2019',
               #'news_upos_skipgram_300_5_2019',
               #'araneum_none_fasttextcbow_300_5_2018'
             ]
    filepath = '../RED_WHITE.txt'
    for i in range(len(models)):
        print("-"*100)
        direct = models[i] + '_WHITE_SYNON_2'
        get_distant(models[i], direct, filepath, FIND_NEIGHBOUR, PART_OF_SPEECH)
if __name__ == "__main__":
    main()

