import csv

def open_scv_statistics(filepath):
    node = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=',')

        for row in reader:
            main_word = row['token']
            if main_word not in node.keys():
                node[main_word] = 0
                node[main_word] += int(row['freq'])

    return node

