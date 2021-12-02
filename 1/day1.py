
def main():
    f = open("day1_input.txt")

    strings = f.readlines()
    data = [int(x) for x in strings]

    # === part 1 ===

    pair1 = data[0:-1]
    pair2 = data[1:]

    comp = zip(pair1, pair2)

    ascending = 0
    for p in comp:
        if p[0] < p[1]:
            ascending += 1

    print(f"part 1: {ascending}")

    # === part 2 ===

    d2 = []

    for i in range(len(data)):
        tmp_sum = 0
        for j in range(0,3):
            try:
               tmp_sum += data[i+j]
            except:
                pass

        d2.append(tmp_sum) 

    pair1 = d2[0:-1]
    pair2 = d2[1:]

    comp = zip(pair1, pair2)

    ascending = 0
    for p in comp:
        if p[0] < p[1]:
            ascending += 1


    print(f"part 2: {ascending}")


    return


if __name__ == "__main__": 
    main()