import sys

f = open(sys.argv[1], 'r')

for line in f:
    two = line[:2]
    if two == "AA":
        k = line.strip().split()
        print(k[:2])
        print(" ".join(k[3:]))
    else:
        print(line.strip())

f.close()
