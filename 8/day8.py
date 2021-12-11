from collections import Counter

def load_data(file):
    lines = file.readlines()
    data = []
    for line in lines:
        first, second = line.split('|')
        data.append( (first.split(), second.split()) )
    return data

def count_unique( data ):
    count = 0
    unique_lengths = [2,3,4,7]
    for test, res in data:
        for item in res:
            if len(item) in unique_lengths:
                count += 1
    return count

def get_bar1(test):
    collect = ""
    for val in test:
        if len(val) == 2:
            collect += val
        elif len(val) == 3:
            collect += val
    col = Counter([c for c in collect])
    out = None
    for k,v in col.items():
        if v == 1:
            out = k
    return out

def get_one(test):
    one = ''
    for val in test:
        if len(val) == 2:
            one = val
    return one

def get_bar2_and_bar4(test, one, bar1):
    four = ''
    five1 = ''
    five2 = ''
    five3 = ''
    for val in test:
        if len(val) == 4:
            four = val
        if len(val) == 5:
            if not five1:
                five1 = val
                continue 
            if not five2:
                five2 = val
                continue
            if not five3:
                five3 = val
                continue

    # print(four, five1, five2, five3)

    four_o = four

    col = Counter([c for c in four+five1+five2+five3])
    bar4 = None
    for k,v in col.items():
        if v == 4:
            bar4 = k

    col = Counter([c for c in four+one+bar4])
    bar2 = None
    for k,v in col.items():
        if v == 1:
            bar2 = k

    return bar2, bar4

def get_bar7_and_five(test, one, bar1, bar2, bar4):
    found = one+bar1+bar2+bar4
    five1 = ''
    five2 = ''
    for val in test:
        if len(val) == 5:
            if not five1:
                five1 = val
                continue 
            if not five2:
                five2 = val
                continue

    five1_o = five1
    five2_o = five2

    for char in [c for c in found]:
        five1 = five1.replace(char,"")
        five2 = five2.replace(char,"")

    five = ''
    bar7 = ''
    if len(five1) == 1:
        bar7 = five1
        five = five1_o
    elif len(five2) == 1:
        bar7 = five2
        five = five2_o

    return bar7, five

def get_bar6(bar1, bar2, bar4, bar7, five):
    val = bar1+bar2+bar4+bar7
    for char in [c for c in val]:
        five = five.replace(char,"")

    return five

def get_bar3(bar6,one):
    return one.replace(bar6,"")

def get_bar5(test, bar1, bar2, bar3, bar4, bar6, bar7):
    eight = ''
    for val in test:
        if len(val) == 7:
            eight = val

    val = bar1+bar2+bar3+bar4+bar6+bar7
    for char in [c for c in val]:
        eight = eight.replace(char,"")    

    return eight    

class SevenSegment:
    def __init__(self, bar1, bar2, bar3, bar4, bar5, bar6, bar7):
        self.bar1 = bar1
        self.bar2 = bar2
        self.bar3 = bar3
        self.bar4 = bar4
        self.bar5 = bar5
        self.bar6 = bar6
        self.bar7 = bar7

    def build_one(self):
        output = ""
        output += self.bar3
        output += self.bar6
        return output

    def build_two(self):
        output = ""
        output += self.bar1
        output += self.bar3
        output += self.bar4
        output += self.bar5
        output += self.bar7
        return output

    def build_three(self):
        output = ""
        output += self.bar1
        output += self.bar3
        output += self.bar4
        output += self.bar6
        output += self.bar7
        return output

    def build_four(self):
        output = ""
        output += self.bar2
        output += self.bar3
        output += self.bar4
        output += self.bar6
        return output

    def build_five(self):
        output = ""
        output += self.bar1
        output += self.bar2 
        output += self.bar4
        output += self.bar6
        output += self.bar7
        return output

    def build_six(self):
        output = ""
        output += self.bar1
        output += self.bar2 
        output += self.bar4
        output += self.bar5
        output += self.bar6
        output += self.bar7
        return output
    
    def build_seven(self):
        output = ""
        output += self.bar1
        output += self.bar3
        output += self.bar6
        return output

    def build_eight(self):
        output = ""
        output += self.bar1
        output += self.bar2 
        output += self.bar3 
        output += self.bar4
        output += self.bar5
        output += self.bar6
        output += self.bar7
        return output
    
    def build_all_numbers(self):
        output = []
        output.append( self.build_one() )
        output.append( self.build_two() )
        output.append( self.build_three() )
        output.append( self.build_four() )
        output.append( self.build_five() )
        output.append( self.build_six() )
        output.append( self.build_seven() )
        output.append( self.build_eight() )
        # numbers = [1,2,3,4,5,6,7]
        # return (numbers, output)
        return output


def determine_config(test):
    bar5 = ''
    bar6 = ''

    # print(test)

    one = get_one(test)
    bar1 = get_bar1(test)
    bar2, bar4 = get_bar2_and_bar4(test, one, bar1)
    bar7, five = get_bar7_and_five(test, one, bar1, bar2, bar4)
    bar6 = get_bar6(bar1, bar2, bar4, bar7, five)
    bar3 = get_bar3(bar6, one)
    bar5 = get_bar5(test, bar1, bar2, bar3, bar4, bar6, bar7)

    session = SevenSegment(bar1, bar2, bar3, bar4, bar5, bar6, bar7)

    # print(f" {bar1} ")
    # print(f"{bar2} {bar3}")
    # print(f" {bar4} ")
    # print(f"{bar5} {bar6}")
    # print(f" {bar7} ")

    #  1-
    # 2- 3-
    #  4-
    # 5 6-
    #  7-

    return session

def compare(res_item, thing):
    count = 0
    for c in res_item:
        if c in thing:
            count += 1


    # print("--",res_item, thing)
    # print("--", count, len(thing))
    # if count == len(thing):
    #     # print("*")
    #     return True
    # else:
    #     return False

def get_output_number(session, res):
    all_num = session.build_all_numbers()
    # print(all_num)
    # print(res)
    # print(len(res))
    # count = 0
    output = ""
    for number in res:
        for n in all_num:
            # print("*")
            # print(n, number)

            if compare(n, number) and (len(n) == len(number)):
                # print(n, number)
                # print("*")
                output += str(all_num.index(n))
        # count += 1
    
    return output

def get_all_output_values( data ):
    values = []
    for test, res in data:
        # print(test,"|",res)
        print(res)
        sesh = determine_config(test)
        number = get_output_number(sesh, res)
        print(number)



        # break
    #     values.append( get_value(test, res) )

    # return values




def main():
    # f = open("day8_input.txt")
    f = open("sample8.txt")
    data = load_data(f)

    print("part 1:",count_unique(data))
    print()
    # print(sum(get_all_output_values(data)))
    get_all_output_values(data)

    
    return

if __name__ == "__main__": 
    main()