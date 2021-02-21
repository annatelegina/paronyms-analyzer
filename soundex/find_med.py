import sys
f = open(sys.argv[1], 'r')
med = int(sys.argv[2])

i = 0
print("Words with sound distance ", med)
for line in f:
    a = line.strip().split()
    if int(a[2]) == med:
        print(a[0], a[1])
        i += 1

print("Total number of pairs:", i)
