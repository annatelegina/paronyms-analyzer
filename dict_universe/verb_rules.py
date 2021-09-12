import sys

PART_OF_SPEECH = '2'
MODE = "red"

attention_suff = ["ЕСТВ", "ИЧ", "ОЧ", "ОМ", "НИЧ"]

def main():
    f = open(sys.argv[1], 'r')
    for line in f:
        b = line.strip()
        if MODE == "red":
            a = b.split()
            word = a[-1]
            if a[1] != PART_OF_SPEECH:
                continue
        else:
            word = a
        part_words = word.split("*")
        end = part_words[-1]
        if end == "ЧЬ" or end == "ТИ" or end == "ТЬ":
            #print(b)
            continue

        first = part_words[0].split("+")
        pref = first[0]
        root_suf = first[-1]
        suf = root_suf.split("-")

        if len(suf) == 1 or suf[-1] in attention_suff:
            beg = pref + "+" if pref != "" else "+"
            new_word = beg + root_suf + "-" + end[0] + "*" + end[1:]
            first_part =  " ".join(a[:-1])
            print(first_part + " " + new_word)
        else:
            last_suf = suf[-1] + end[0]
            beg = pref + "+" if pref != "" else "+"
            new_word = beg + "-".join(suf[:-1]) + "-" + last_suf + "*" + end[1:]
            first_part = " ".join(a[:-1])
            print(first_part + " " + new_word)
    f.close()


if __name__ == "__main__":
    main()
