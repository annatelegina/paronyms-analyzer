import sys

f = open(sys.argv[1], 'r')


res = []
s = 0
n = 0
symb = ","
i = 0
for line in f:
    a = line.strip().split(" ")
    num = float(a[2])
    s += num
    res.append(num)
    n += 1

res.sort()

print("Min: ", res[0], "max: ", res[-1], " mediana: ", res[(len(res)-1)//2], "mean: ", s/n)

f.close()
