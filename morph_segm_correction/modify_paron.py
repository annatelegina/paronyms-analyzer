import sys

f = open(sys.argv[1], 'r')
seen = set()
for line in f:
    #print(line)
    a = line.strip().split()
    POS = int(a[1])
    #seen = set()

    if a[0] == "AA":
        word = a[2].strip().lower()
    else:
        word = "".join(c for c in a[-1] if c.isalpha()).lower()
    #print(word)
    if word not in seen:
        print(line.strip())
        seen.add(word)



    """
    if POS == 2:
        if a[0] == "AA":
            first = a[:3]
            second = a[3:-1]
            word = a[-1]
            alls, end = word.split("*")
            new = alls + '-' + end[0] + "*" + end[1:]
            print(" ".join(first) + " "+  " ".join(second) + " " + new)
        else:
            symb = ""
            if "ЧЬ" in line:
                symb = "ЧЬ"
            elif "ТЬ" in line:
                symb = "ТЬ"
            elif "ТИ" in line:
                symb = "ТИ"
            a = line.split(symb)
            word = a[0][:-1] + "*" + symb + a[1]
            print(word.strip())
    else:
        print(line.strip())
    """
    """
    if POS == 1:
        if a[0] == "AA":
            if int(a[5]) == 2:
                #print(line)
                continue
            else:
                #pass
                print(line.strip())
        else:
            if int(a[2]) == 2:
                continue
            else:
                print(line.strip())
    else:
        print(line.strip())
    """
    #delete adverbs
    #s = int(a[1])
    #if s == 4:
    #    continue
    #else:
    #    print(line.strip())

f.close()
