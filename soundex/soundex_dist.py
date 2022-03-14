import sys

f = open(sys.argv[1])

count = 0
threshold = -1
all_stat = {}

for line in f:
    a = line.strip().split()
    coef = int(a[2])
    if coef < threshold:
        continue
    print(line.strip())
    if coef in all_stat.keys():
        all_stat[coef] += 1
    else:
        all_stat[coef] = 1
f.close()
print(all_stat)
