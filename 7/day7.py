def get_fuel_cost(positions, loc):
    return sum( [abs(pos-loc) for pos in positions] )

def get_updated_fuel_cost(positions, loc):
    return sum( [sum(range(1,abs(pos-loc)+1)) for pos in positions] )

def naive(positions, calc_func):
    positions.sort()
    first = positions[0]
    last = positions[-1]

    lowest_cost = last ** last
    for pos in range(first, last+1):
        val = calc_func(positions, pos)
        if val < lowest_cost:
            lowest_cost = val
    
    return lowest_cost

def main():
    f = open("day7_input.txt")
    # f = open("sample7.txt")
    positions = [int(x) for x in f.readlines()[0].split(',')]

    print(naive(positions, get_fuel_cost))
    print(naive(positions, get_updated_fuel_cost))
    
    return

if __name__ == "__main__": 
    main()