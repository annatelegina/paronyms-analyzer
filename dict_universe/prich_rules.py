import sys

PART_OF_SPEECH = '2'

def check_pairs(suf):
    comb_set1 = [
                    ["ЫВ", "АВШ"],
                    ["ЫВ", "АЮЩ"],
                    ["ОВ", "АВШ"],
                    ["ОВ", "АЮЩ"],
                    ["ЫВ", "АНИ"], 
                    ["ОВ", "АЮЩ"],
                    ["Н", "УВШ"],
                    ["ОВ", "АНН"]
                ]
    comb_set2 = [
                    ["ОВАН", "Н"],
                ]
    s = [suf[-2], suf[-1]]
    new = []
    for c in comb_set1:
        if c == s:
            new = [s[0] + s[1][0], s[1][1:]]
            break
    for c in comb_set2:
        if c == s:
            new = [s[0][:-1], s[0][-1] + s[1]]
            break

    if len(new) > 0:
        return True, suf[:-2] + new
    else:
        return False, suf

def check_spliting(suf):
    comb_set1 = [
                    "УЮЩ",
                    "УВШ",
                    "ИВШ", 
                    "ЕВШ", 
                    "ЯВШ",
                    "ЕЮЩ",
                    "АЮЩ",
                    "АЕМ",
                    "УЕМ",
                    "АВШ", 
                    "АНН", 
                    "ЯНН", 
                    "НУТ", 
                ]
    s = suf[-1]
    new = []
    for c in comb_set1:
        if c == s:
            if s != "НУТ":
                new = [s[0], s[1:]]
            else:
                new = [s[:-1], s[-1]]
            break

    if len(new) > 0:
        return True, suf[:-1] + new
    else:
        return False, suf



def main():
    f = open(sys.argv[1], 'r')
    for line in f:
        b = line.strip()
        a = b.split()
        word = b
        part_words = word.split("*")
        end = part_words[-1]
        first = part_words[0].split("+")
        pref = first[0]
        root_suf = first[-1]
        suf = root_suf.split("-")
        root = suf[0]
        suffixes = suf[1:]
        changed = False
        if len(suffixes) >= 2:
            changed, new_s = check_pairs(suffixes)
        if not changed and len(suffixes) > 0:
            changed, new_s = check_spliting(suffixes)

        if changed:
            #print(end)
            s = pref + "+" +  root + "-" + "-".join(new_s) + "*" + end
        else:
            s = b
        print(s)

    f.close()


if __name__ == "__main__":
    main()
