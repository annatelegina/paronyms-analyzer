import requests

#-----------------------------------------------------------------------
#-----------------------------Word2Vec utils----------------------------
#-----------------------------------------------------------------------

def api_similarity(m, w1, w2):
    url = '/'.join(['https://rusvectores.org', m, w1 + '__' + w2, 'api', 'similarity/'])
    r = requests.get(url, stream=True)
    a = r.text.split('\t')[0]
    return a

def api_neighbor(m, w, f):
    neighbors = []
    count = 0
    url = '/'.join(['http://rusvectores.org', m, w, 'api', f]) + '/'
    r = requests.get(url=url, stream=True)
    for line in r.text.split('\n'):
        count += 1
        if count > 2:
            k = line.split()
            if len(k) > 1:
                #print(k[0])
                neighbors.append((k[0], k[1]))
    return neighbors

def search_word(model, w1, w2, FORMAT='csv'):
    neighbors = api_neighbor(model, w1, FORMAT)
    #w = w2.decode('ascii')
    w = w2
   # print(w)
    for ind in range(len(neighbors)):
        #print(neighbors[ind][0])
        if neighbors[ind][0] == w:
            return 'Yes'
    return 'No'

