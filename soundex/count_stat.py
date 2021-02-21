import sys

def main():
    meanings = [0 for i in range(12)]
    values = []
    f = open(sys.argv[1], 'r')
    stat = {
            "max": 0, 
            "max_pairs": [],
            "min": 0,
            "min_pairs": [],
            "sum": 0, 
            "num": 0
            }

    first = True
    for line in f:
        x, y, dist = line.strip().split()
        dist = int(dist)
        meanings[dist] += 1
        values.append(dist)
        if first:
            stat["min"] = dist
            stat["min_pairs"].append((x, y))
            first = False

        if dist > stat["max"]:
            stat["max"] = dist
            stat["max_pairs"] = [(x, y)]
        elif dist == stat["max"]:
            stat["max_pairs"].append((x, y))

        if dist < stat["min"]:
            stat["min"] = dist
            stat["min_pairs"] = [(x, y)]
        elif dist == stat["min"]:
            stat["min_pairs"].append((x, y))

        stat["sum"] += dist
        stat["num"] += 1

    print("===> Statistics: ")

    print("Max: ", stat["max"])
    for x, y in stat["max_pairs"]:
        print(x, y)
    
    print("Min: ", stat["min"])
    for x, y in stat["min_pairs"]:
        print(x, y)

    values.sort()
    print("Mean: ", stat["sum"]/stat["num"])
    print("Mediana : ", values[(len(values)-1)//2])
    print("Stat: ", meanings)
    f.close()

if __name__ == "__main__":
    main()

