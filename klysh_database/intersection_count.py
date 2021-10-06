import os
import math
def from_tuples_to_dict(inputs):
    d = {}
    for t in inputs:
        w, fr = t
        d[w] = fr

    return d, len(inputs)

def col_intersection(set1, set2, w1, w2, main_words, tail_words, measure, threshold):

    """
    elif measure == "log-dise":
        for k1 in set1.keys():
            m = 2 * set1[k1] /(main_words[w1] + tail_words[k1])
            m = math.log2(m) + 30
            if m > threshold:
                new_set1[k1]  = m

        for k1 in set2.keys():
            m = 2 * set2[k1] /(main_words[w2] + tail_words[k1])
            m = math.log2(m) + 30
            if m > threshold:
                new_set2[k1]  = m

    """

    intersec = {}
    cap = 0

    for k1 in set1.keys():
        if k1 in set2.keys():
            cap += 1
            intersec[k1] = (set1[k1], set2[k1])

    return intersec, cap
