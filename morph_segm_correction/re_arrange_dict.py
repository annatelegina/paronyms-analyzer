import os
import csv
import sys
import glob
import math

sys.path.append("..")
sys.path.append("../klysh_database")
sys.path.append("../utils")

from parse_dict import *
from intersection_count import *
from kol_utils import *
from connect import *
from csv_utils import *

def read_file(path):
    d = {}

    f = open(path, 'r')
    for line in f:
        a = line.strip().lower().split()
        if not a:
            continue
        d[a[0]] = (a[1], a[2])

    return d


pos = None 
dict_path = "../NEW_RED_FIXED.txt"
pairs = parse_dict(dict_path, pos=pos)
f = open(dict_path, 'r')
strings = []
for line in f:
    strings.append(line)

dict_p = open(dict_path,'r')
for line in dict_p:
    strings.append(line.strip())
dict_p.close()

i = 0
new_file = sys.argv[1]

new_words = read_file(new_file)
for p in pairs:
    words = p[1]
    for w in words:
        parts = " ".join(strings[i].split()[:4])
        old = strings[i].split()[4]
        if w in new_words.keys():
            new_w = new_words[w][0].split("/")
            col = []
            for p_ in new_w:
                ww, part = p_.split(":")
                if part == "pref":
                    col.append("-")
                elif part == "root":
                    col.append("+")
                elif part == "suff":
                    col.append("-")
                elif part == "end":
                    col.append("*")
                col.append(ww)
            if old[-1] == "*":
                col.append("*")
            #print(parts, "".join(col).upper())
        else:
            print(p[0], w, strings[i])
        i += 1
