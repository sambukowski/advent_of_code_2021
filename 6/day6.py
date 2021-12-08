import numpy as np
from collections import Counter

class Habitat:
    def __init__(self, list_of_init_fish):
        self.fish = np.array( list_of_init_fish )

    def count_zeros(self):
        return (self.fish == 0).sum()

    def update_zeros(self):
        self.fish = np.where(self.fish == 0, 7, self.fish)
    
    def append_new_fish(self, count):
        arr = np.ones(count, dtype=int)
        arr = arr * 8
        self.fish = np.append( self.fish, arr )

    def dec_array(self):
        self.fish = self.fish - 1

    def age_fish(self):
        zeros = self.count_zeros()
        self.update_zeros()
        self.dec_array()
        self.append_new_fish( zeros )

    def estimate_pop(self, num_days):
        while num_days > 0:
            self.age_fish()
            num_days -= 1
            # print(f"Days left: {num_days}")
        return self.fish.size

    def __str__(self):
        output = "Fish: "
        list_fish = self.fish.tolist()
        for fish in list_fish:
            output += f"{fish} "
        return output

# alex's code because i can't figure this out
# dictionaries are hard
def simulate(fish_pool, days):
    fish_dict = Counter(fish_pool)
    for x in range(days):
        print(fish_dict)
        updated_fish = {}
        if 0 in fish_dict:
            updated_fish[6] = updated_fish[8] = fish_dict[0]
        for age in range(1, 9):
            if age in fish_dict:
                if (age == 7) and (6 in updated_fish):
                    updated_fish[6] += fish_dict[age]
                else:
                    updated_fish[age-1] = fish_dict[age]
        fish_dict = updated_fish
    return sum(fish_dict.values())

def main():
    f = open("day6_input.txt")
    # f = open("sample6.txt")
    fish_pool = [int(x) for x in f.readlines()[0].split(',')]

    # naive part 1
    # habitat = Habitat( initial_fish )
    # num_days = 80
    # print(f"Fish population after {num_days} days: {habitat.estimate_pop(num_days)}")
    print(f'Part 1: {simulate(fish_pool, 10)}')


    # print(f'Part 1: {simulate(fish_pool, 80)}')
    # print(f'Part 2: {simulate(fish_pool, 256)}')


    return

if __name__ == "__main__": 
    main()