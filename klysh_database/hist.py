import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import sys

f = open(sys.argv[1], "r")

vals = []
for i in f:
    a = i.strip().split()
    vals.append(float(a[2]))

vals.sort()

x = []
i = 0.1
start = 0
while i <= 1:
    begin = start
    while start < len(vals) and vals[start] < i:
        start += 1

    x.append(start - begin)
    i += 0.1

f.close()


y = [i for i in range(len(x))]

num_bins = len(x)
print(x, y)
fig, ax = plt.subplots()

ax.bar(y, x)

plt.title("All paronyms collocation statistics")
plt.ylabel("Frequency")
plt.xlabel("distances based on log-dise ranking")
plt.savefig("log-dise_threshold_10" + ".pdf", format='pdf')

