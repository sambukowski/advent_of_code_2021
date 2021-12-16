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


class SevenSegment:
    def __init__(self, bar1, bar2, bar3, bar4, bar5, bar6, bar7):
        self.bar1 = bar1
        self.bar2 = bar2
        self.bar3 = bar3
        self.bar4 = bar4
        self.bar5 = bar5
        self.bar6 = bar6
        self.bar7 = bar7

        print(f" {self.bar1} ")
        print(f"{self.bar2} {self.bar3}")
        print(f" {self.bar4} ")
        print(f"{self.bar5} {self.bar6}")
        print(f" {self.bar7} ")


    def build_zero(self):
        output = ""
        output += self.bar1
        output += self.bar2
        output += self.bar3
        output += self.bar5
        output += self.bar6
        output += self.bar7
        return output


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

    def build_nine(self):
        output = ""
        output += self.bar1
        output += self.bar2 
        output += self.bar3 
        output += self.bar4
        output += self.bar6
        output += self.bar7
        return output

    
    def build_all_numbers(self):
        output = []
        output.append( self.build_zero() )
        output.append( self.build_one() )
        output.append( self.build_two() )
        output.append( self.build_three() )
        output.append( self.build_four() )
        output.append( self.build_five() )
        output.append( self.build_six() )
        output.append( self.build_seven() )
        output.append( self.build_eight() )
        output.append( self.build_nine() )
        # numbers = [1,2,3,4,5,6,7]
        # return (numbers, output)
        return output

def find_unique(test):
    one = None
    seven = None
    four = None
    eight = None
    for val in test:
        if len(val) == 2:
            one = val
        elif len(val) == 3:
            seven = val
        elif len(val) == 4:
            four = val
        elif len(val) == 7:
            eight = val
    
    return one, four, seven, eight

def get_len_five(test):
    output = []
    for val in test:
        if len(val) == 5:
            output.append(val)
    return output

def get_len_six(test):
    output = []
    for val in test:
        if len(val) == 5:
            output.append(val)
    return output

def get_three(len_fives, seven):
    three = None
    for val in len_fives:
        intersection = [c for c in seven].intersect([c for c in val])
        if len(intersection) == 3:
            three = val
    return three

def determine_config(test):
    zero = one = two = three = four = five = six = seven = eight = nine = None
    one, four, seven, eight = find_unique(test)
    len_fives = get_len_five(test)
    len_sixs  = get_len_six(test)
    three = get_three(len_fives, seven)

    print(f"0 {zero}")
    print(f"1 {one}")
    print(f"2 {two}")
    print(f"3 {three}")
    print(f"4 {four}")
    print(f"5 {five}")
    print(f"6 {six}")
    print(f"7 {seven}")
    print(f"8 {eight}")
    print(f"9 {nine}")



    session = SevenSegment(bar1, bar2, bar3, bar4, bar5, bar6, bar7)

    return session

def compare(res_item, thing):
    arr = [ch for ch in res_item]
    count = 0
    for c in arr:
        if c in thing:
            count += 1

    if len(arr) == count:
        return True
    else:
        return False


    # print("--",res_item, thing)
    # print("--", count, len(thing))
    # if count == len(thing):
    #     # print("*")
    #     return True
    # else:
    #     return False

def get_output_number(session, res):
    all_num = session.build_all_numbers()
    # print(all_num[0])
    # print(all_num[1])
    # print(all_num[2])
    # print(all_num[3])
    # print(all_num[4])
    # print(all_num[5])
    # print(all_num[6])
    # print(all_num[7])
    # print(all_num[8])
    # print(all_num[9])

    # print(all_num)
    # print(res)
    # print(len(res))
    # count = 0
    output = ""
    for number in res:
        if len(number) == 2:
            output += str(1)    # 1
        elif len(number) == 3:
            output += str(7)    # 7
        elif len(number) == 4:
            output += str(4)    # 4
        elif len(number) == 5:
            # 2
            if compare(number,session.build_two()):
                output += str(2)
            # 3
            elif compare(number, session.build_three()):
                output += str(3)
            # 5
            elif compare(number, session.build_five()):
                output += str(5)
        elif len(number) == 6:
            # 0
            if compare(number, session.build_zero()):
                output += str(0)
            # 6
            elif compare(number, session.build_six()):
                output += str(6)
            # 9
            elif compare(number, session.build_nine()):
                output += str(9)
        elif len(number) == 7:
            output += str(8)    # 8
        else: 
            pass
            # for n in all_num:
            #         # print("*")
            #         # print(n, number)

            #         if compare(n, number) and (len(n) == len(number)):
            #             # print(n, number)
            #             # print("*")
            #             output += str(all_num.index(n))
        break
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