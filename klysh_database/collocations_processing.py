import os
import csv
import sys
import glob
import math

from intersection_count import *

directory = sys.argv[1]

files = os.listdir(directory)
threshold = 10

for f in files:
    node = {}
    length = 0
    words = []
    with open(os.path.join(directory, f), newline='') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=',')
        
        for row in reader:
            main_word = row['main_word']
            if main_word not in node.keys():
                node[main_word] = {}
                words.append(main_word)
                length += 1
            tail_word = row['tail_word']
            if tail_word not in node[main_word].keys():
                if int(row['freq']) > threshold:
                    node[main_word][tail_word] = int(row['freq'])

        for i in range(length):
            for j in range(i+1, length):
                cap1 = len(node[words[i]].keys())
                cap2 = len(node[words[i]].keys())
                intersec, cap12 = col_intersection(node[words[i]], node[words[j]])
                print(cap12 / math.sqrt(cap1*cap2))

#    assert False
