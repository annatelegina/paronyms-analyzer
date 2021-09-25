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

pos = 1
dict_path = "../RED.txt"


pairs = parse_dict(dict_path, pos=pos)

main_stat = "../database/adj_nouns_main_dict_inf.csv"
tail_stat = "../database/adj_nouns_tail_dict_inf.csv"

result_dir = "../results_threshold"

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

file_name = "total_info.txt"

threshold = 10

out_file = os.path.join(result_dir, file_name)
result_file = open(out_file, "w+")

main_words = open_scv_statistics(main_stat)
tail_words = open_scv_statistics(tail_stat)

measure = "threshold"

connection = create_connection("cosyco.ru", "cosycoreader", "Rh@cysqIbyibkk@5")


for p in range(len(pairs)):
    w = pairs[p][1]

    l = len(w)
    for i in range(l):
        for j in range(i+1, l):

            w1 = w[i].upper()
            w2 = w[j].upper()
            query = "select tail_word, freq from cosyco_base.adj_noun_comb_inf where cosyco_base.adj_noun_comb_inf.main_word = \"{:s}\" "

            res1, cap1 = from_tuples_to_dict(execute_read_query(connection, query.format(w1)))
            res2, cap2 = from_tuples_to_dict(execute_read_query(connection, query.format(w2)))

            if cap1 == 0 or cap2 == 0:
                k = 0
            else:
                intersec, cap12 = col_intersection(res1, res2, w1, w2, main_words, tail_words,  measure, threshold)
                k = cap12 / math.sqrt(cap1*cap2)
            
            print(w1, w2, k)
 
