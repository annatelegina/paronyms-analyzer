import os
import sys
import xlrd, xlwt

from api import *

def find_unknown(src, model):
    tmp_tag = ["_NOUN", "_VERB", "_ADJ"]
    check_word = ['человек_NOUN', 'делать_VERB', 'красный_ADJ']
    res_words = {
            1: [], 
            2: [], 
            3: []
    }

    book = xlrd.open_workbook(src)

    work_sheet = book.sheet_by_index(0)
    num_rows = work_sheet.nrows - 1
    current_row = 0
    number = 0
    res = [0, 0, 0]
    while current_row < num_rows:
        input_total = ""
        w1 = work_sheet.cell_value(current_row, 0)
        w2 = work_sheet.cell_value(current_row, 1)
        part = int(work_sheet.cell_value(current_row, 2))
        k1 = api_similarity(model, w1 + tmp_tag[part-1], check_word[part-1])
        k2 = api_similarity(model, w2 + tmp_tag[part-1], check_word[part-1])
        if 'nknown' in k1:
            if w1 not in res_words[part]:
                res_words[part].append(w1)
                number += 1
                res[part-1] += 1
            print(w1)
        if 'nknown' in k2:
            if w2 not in res_words[part]:
                res_words[part].append(w2)
                number += 1
                res[part-1] += 1
            print(w2)
        current_row += 1
    
    print(model)
    print("-"*50)
    print("Total number of unknown words:", number)
    print("Nouns: ", res[0], "Adj: ", res[1], "Verbs: ", res[2])
    print(res_words)
    print()


def main():
    models = [ #'tayga_upos_skipgram_300_2_2019',
               #'ruscorpora_upos_cbow_300_20_2019',
               #'ruwikiruscorpora_upos_skipgram_300_2_2019',
               #'tayga_none_fasttextcbow_300_10_2019',
               'news_upos_skipgram_300_5_2019',
               #'araneum_none_fasttextcbow_300_5_2018'
             ]
    filepath = sys.argv[1]
    for i in range(len(models)):
        find_unknown(filepath, models[i])
if __name__ == "__main__":
    main()

