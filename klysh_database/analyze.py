import sys

f = open(sys.argv[1], 'r')
for l in f:
    a = l.strip()
    if a.count("*") == 0:
        a += "*"
    if a[1:].count("+") > 1:
        k = a.split()
        w = k[-1]
        a = " ".join(k[:4]) + " " + "-" + w[1:]

    print(a)


