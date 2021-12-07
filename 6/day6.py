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

# class FishBowl:
#     def __init__(self, list_fish):
#         keys   = Counter(list_fish).keys()   # spawn days
#         values = Counter(list_fish).values() # count with that value

#         inputs = zip(keys, values)

#         self.mature_fish = [FishCounter(p[0], p[1]) for p in inputs]
#         self.baby_fish = []

#     def age_fish(self):
#         new_baby_fish = []
#         zero_count_index = None
#         index = 0
#         # age the mature fish and keep track of the new ones
#         for counter in self.mature_fish:
#             if counter.spawn_days == 0:
#                 zero_count_index = index    # there should only ever be one counter at zero 
#             spawned = counter.age()
#             if spawned > 0:
#                 new_baby_fish.append( BabyFish(spawned) )
#             index += 1

#         # merge counter check to make sure there is only one counter for each possible cycle


#         # check if the baby fish have grown up and can be added 
#         to_remove = []
#         index = 0
#         for baby in self.baby_fish:
#             spawned = baby.age()
#             if spawned > 0:
#                 to_remove.append( index )
#                 self.mature_fish[zero_count_index].count += spawned
#             index += 1

#         # remove the newly grown up babys
#         to_remove.reverse()
#         for i in to_remove:
#             self.baby_fish.pop(i)

#     def add_grown_babies(self, zero_index, count):
#         return



# class FishCounter:
#     def __init__(self, spawn_days, count ):
#         self.spawn_days = spawn_days
#         self.count = count

#     def age(self):
#         if self.spawn_days == 0:
#             self.spawn_days = 6
#             return self.count
#         else:
#             self.spawn_days -= 1
#             return 0
            
#     def include_new(self, new_count):
#         if self.spawn_days == 0:
#             self.count += new_count

# class BabyFish:
#     def __init__(self, count):
#         self.spawn_days = 8
#         self.count = count

#     def age(self):
#         if self.spawn_days == 0:
#             self.spawn_days = -1
#             return self.count
#         else:
#             self.spawn_days -= 1
#             return 0

class FishBowl:
    def __init__(self, list_fish):
        self.baby_fish = {}

        keys   = Counter(list_fish).keys()   # spawn days
        values = Counter(list_fish).values() # count with that value

        inputs = zip(keys, values)
        self.data = {6:0}
        for k,v in inputs:
            self.data.update({k:v})

        print(self.data)
        babies = self.age_fish()
        print(self.data, babies)
        babies = self.age_fish()
        print(self.data, babies)
    
    def age_fish(self):
        new_fish_count = None
        tmp_dict = {}
        for k,v in self.data.items():
            if k == 0:
                new_fish_count = v
                k = 7
            tmp_dict.update({k-1:v})

        self.data = tmp_dict
        return new_fish_count

    # add to the baby array
    # collect from the baby array and add the mature array

def main():
    f = open("day6_input.txt")
    # f = open("sample6.txt")
    strings = f.readlines()
    initial_fish = [int(x) for x in strings[0].split(',')]

    # naive part 1
    habitat = Habitat( initial_fish )
    num_days = 80
    # print(f"Fish population after {num_days} days: {habitat.estimate_pop(num_days)}")

    fb = FishBowl(initial_fish)


    return

if __name__ == "__main__": 
    main()