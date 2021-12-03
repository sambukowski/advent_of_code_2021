
def main():
    f = open("day2_input.txt")

    strings = f.readlines()
    data = [(x.split()[0], int(x.split()[1])) for x in strings]

    # === part 1 ===

    depth = 0
    position = 0

    for item in data:
        if "forward" in item[0]:
            position += item[1]
        elif "down" in item[0]:
            depth += item[1]
        elif "up" in item[0]:
            depth -= item[1]

    value = position * depth
    print(f"day2 part 1: {value}")

    # === part 2 ===

    depth = 0
    position = 0
    aim = 0 

    for item in data:
        if "forward" in item[0]:
            position += item[1]
            depth += aim * item[1]
        elif "down" in item[0]:
            aim += item[1]
        elif "up" in item[0]:
            aim -= item[1]

    value = position * depth
    print(f"day2 part 2: {value}")

    return


if __name__ == "__main__": 
    main()