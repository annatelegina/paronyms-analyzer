import os
import csv
import sys
import glob
import math

sys.path.append("..")
sys.path.append("../utils")

from parse_dict import *
from intersection_count import *
from kol_utils import *
from connect import *
from csv_utils import *

pos = 2
#dict_path = "../RED.txt"
#pairs = parse_dict(dict_path, pos=pos)

dict_path = sys.argv[1]  # "../database/evaluate_nouns.txt"
pairs = parse_file(dict_path)

result_dir = sys.argv[2] #"../results_stat"

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

file_name = "total_info.txt"
measure = "log-dise"

top = 100

out_file = os.path.join(result_dir, file_name)
result_file = open(out_file, "w+")
result_file.write("Top " + str(top) + "\n")

main_stat = "../database/adj_nouns_main_dict_inf.csv"
tail_stat = "../database/adj_nouns_tail_dict_inf.csv"
if pos == 1:
    main_words = open_scv_statistics(main_stat)
    tail_words = open_scv_statistics(tail_stat)
elif pos == 2:
    main_words = open_scv_statistics(tail_stat)
    tail_words = open_scv_statistics(main_stat)

connection = create_connection("cosyco.ru", "cosycoreader", "Rh@cysqIbyibkk@5")


for p in range(len(pairs)):
    w = pairs[p][1]

    l = len(w)
    for i in range(l):
        for j in range(i+1, l):

            w1 = w[i].upper()
            w2 = w[j].upper()
            if pos == 1: #noun
                query = "select tail_word, freq from cosyco_base.adj_noun_comb_inf where cosyco_base.adj_noun_comb_inf.main_word = \"{:s}\" "
            elif pos == 2: #adj
                query = "select main_word, freq from cosyco_base.adj_noun_comb_inf where cosyco_base.adj_noun_comb_inf.tail_word = \"{:s}\" "
            res1 = execute_read_query(connection, query.format(w1))
            res2 = execute_read_query(connection, query.format(w2))

            if measure == "log-dise":
                new1 = []
                for p in range(len(res1)):
                    ww, fr = res1[p]
                    if w1 in main_words.keys() and ww in tail_words.keys():
                        m = 2 * fr /(main_words[w1] + tail_words[ww])
                    else:
                        m = 1
                    m = math.log2(m)
                    new1.append((ww, fr, m))
                new2 = []
                for p in range(len(res2)):
                    ww, fr = res2[p]
                    m = 2 * fr / (main_words[w2] + tail_words[ww])
                    m = math.log2(m)
                    new2.append((ww, fr, m))

                res2 = new2
                res1 = new1
            res1.sort(key=lambda x: -x[2])
            res2.sort(key=lambda x: -x[2])

            if top < len(res1):
                res1 = res1[:top]
            if top < len(res2):
                res2 = res2[:top]

            csv_write_table(result_dir, w1 + "_" + w2, res1, res2)
            
            res1, cap1 = from_tuples_to_dict(res1)
            res2, cap2 = from_tuples_to_dict(res2)

            if cap1 == 0 or cap2 == 0:
                k = 0
            else:
                intersec, cap12 = col_intersection(res1, res2)
                k = cap12 / top

            result_file.write(w1 +  " " + w2 + " " + str(k) + "\n")
            print(w1, w2, k)
 
