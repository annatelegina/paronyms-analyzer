import sys

def delete_symbols(word, kind='word'):
    if kind == 'word':
        new = ''
        for c in word:  
            if c not in ('*','-','+','1','2','3','4','5','6'):
                new += c
    elif kind == 'morph':
        new = Morph(word)
    return new

class Morph(object):
    
    def __init__(self, word):
        self.preffix = []
        self.suffix = []
        self.word = delete_symbols(word, kind='word').lower()
        word = word.split('+')
        if word[0]:
            p = word[0].split('-')
            for i in range(1, len(p)):
                self.preffix.append(p[i].lower())
        aff = word[1].split('-') if '-' in word[1] else [word[1]]
        for i in range(len(aff)):
            if '*' in aff[i]:
                parse = aff[i].split('*')
           #     print(parse)
                s = parse[0]
                self.end = parse[1].lower() if len(parse) > 1 else None
            else:
                s = aff[i]
            if i == 0:
                self.root = s.lower()
            else:
                self.suffix.append(s.lower())


