import sys

f = open(sys.argv[1], 'r')

symb = "-ОСТ*Ь"
new = "-ОСТЬ*"

for i in f:
    
    if symb in i:
        new_s = i.replace(symb, new)

        print(new_s.strip())
    else:
        #if '*' not in i:
        #    i = i.strip() + '*'
        print(i.strip())
        #pass
f.close()
