import os
import math


def from_tuples_to_dict(inputs, metrics="dice"):
    d = {}
    i = 1
    for t in inputs:
        w, fr, log = t
        if metrics != "dice":
            d[w] = i
        else:
            d[w] = log
        i += 1

    return d, len(inputs)

def col_intersection_rank(set1, set2):
    intersec = {}
    cap = 0
    acc = 0
    ones = 0
    for k1 in set1.keys():
        if k1 in set2.keys():
            ones += 1
            cap += (1/set1[k1])
            #cap += acc
            #print ones, acc, cap)
            intersec[k1] = (set1[k1], set2[k1])
            
    cap = cap/len(list(set1.keys()))
    return intersec, cap


def col_intersection(set1, set2, metrics="dice"):

    if metrics == "rank":
        i, c = col_intersection_rank(set1, set2)
        return i, c

    intersec = {}
    cap = 0
    ss = 0
    for k1 in set1.keys():
        ss += set1[k1]
        if k1 in set2.keys():
            if metrics == "dice":
                #print(set1[k1])
                cap += set1[k1]
            else:
                cap += 1
            intersec[k1] = (set1[k1], set2[k1])

    if metrics == "dice":
        #print(ss, cap)
        cap = cap / ss

    return intersec, cap
