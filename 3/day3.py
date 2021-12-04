
def remain_by_bit(pos, data, keep):
    remaining = [x for x in data if int(x[pos])==keep]
    return remaining

def get_most_common_at_pos(pos,data, tie_break=1):
    count = 0
    length = len(data)

    for row in data:
        if int(row[pos]) == 1:
            count += 1

    if count > (length/2):
        return 1
    elif count == (length/2):
        return tie_break
    else:
        return 0

def main():
    f = open("day3_input.txt")

    strings = f.readlines()
    data = strings

    # === part 1 ===

    length_row = len(data[0])
    length_data = len(data)
    values = [0] * (length_row-1)

    for row in data:
        for i in range(0,length_row-1):
            if int(row[i]) == 1:
               values[i] += 1

    pos_bit_count = [0] * (length_row-1)
    for i in range(0,length_row-1):
        if values[i] > (length_data/2):
            pos_bit_count[i] = 1

    print(length_data, values)
    
    gamma = int("".join(str(x) for x in pos_bit_count), 2)
    tmp_eps = [1 if x==0 else 0 for x in pos_bit_count]
    epsilon = int("".join(str(x) for x in tmp_eps), 2)

    print(pos_bit_count, gamma)
    print(tmp_eps, epsilon)

    value = gamma * epsilon
    print(f"day3 part 1: {value}")

    # === part 2 ===

    remaining = data
    for i in range(0,length_row-1):
        keep = get_most_common_at_pos(i,remaining)
        if len(remaining) == 1:
            break
        remaining = remain_by_bit(i, remaining, keep)
        print(i, keep, len(remaining))


    oxygen_gen = int(remaining[0], 2)
    print(remaining, oxygen_gen)

    remaining = data
    for i in range(0,length_row-1):
        keep = get_most_common_at_pos(i,remaining)
        keep = (1 if keep==0 else 0)
        if len(remaining) == 1:
            break
        remaining = remain_by_bit(i, remaining, keep)
        print(i, keep, len(remaining))


    co2_gen = int(remaining[0], 2)
    print(remaining, co2_gen)

    value = oxygen_gen * co2_gen
    print(f"day3 part 2: {value}")

    return


if __name__ == "__main__": 
    main()