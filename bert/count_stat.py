import sys

FILE = sys.argv[1]

f = open(FILE, 'r')

stat = 0
min_v = 100
max_v = -1
all_v = []
count = 0

for line in f:
    a = line.strip().split()
    k = float(a[2])
    stat += k
    count += 1
    all_v.append(k)
    if min_v > k:
        min_v = k
    if max_v < k:
        max_v = k

all_v.sort()

f.close()

print("RESULT")
print("Mean:", stat/count)
print("Max:", max_v, "min:", min_v)
print("Med:", all_v[len(all_v)//2])

