import os

def col_intersection(set1, set2):
    intersec = {}
    cap = 0

    for k1 in set1.keys():
        if k1 in set2.keys():
            cap += 1
            intersec[k1] = (set1[k1], set2[k1])


    return intersec, cap
