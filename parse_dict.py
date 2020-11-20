from morph import *

def delete_symbols(word, kind='word'):
    if kind == 'word':
        new = ''
        for c in word:
            if c not in ('*','-','+','1','2','3','4','5','6'):
                new += c
    elif kind == 'morph':
        new = Morph(word)
    return new


def parse_dict(filepath, kind='word'): 
    #kind : word or lists of prefixes, affixes and suffixes
    f = open(filepath, 'rb')
    i = 0
    paronims = []
    main = ''
    pairs = []
    first = True
    help_coef = 0
    for x in f:
        natural_dec = x.decode('utf-8')
        s = natural_dec.strip().split()
        word = delete_symbols(s[4], kind)
        if kind == 'word':
            word = word.lower()
        if s[0] == '+':
            if not first:
                paronims.append((help_coef, pairs))
            help_coef = int(s[1])
            pairs = []
            pairs.append((s[2], s[3], word))
            first = False
        else:
            first = False
            pairs.append((s[2], s[3], word))
        i += 1
        #if i > 20:
         #   break
    f.close()
    return paronims
