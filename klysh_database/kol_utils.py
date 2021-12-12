import csv

def open_scv_statistics(filepath, pos=1):
    node = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=',')

        for row in reader:
            #print(row)
            main_word = row['token']
            if main_word not in node.keys():
                node[main_word] = 0
                node[main_word] += int(row['freq'])

    return node

def parse_file(filepath):
    res = []
    f = open(filepath)

    for line in f:
        w = []
        nouns = line.strip().split('-')
        for n in nouns:
            word = n.strip()
            w.append(word)

        res.append((1, w))

    return res
