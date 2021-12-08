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
        # print(res)
        for item in res:
            if len(item) in unique_lengths:
                count += 1
    return count

def get_one(test):
    # get which letter represents bar 1
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

#  1
# 2 3
#  4
# 5 6
#  7

# [bar1] get bar1 using 1 and 7 
# [bar4] figure out bar4 from 5long that has all vals from 7 and shares with 4
# [bar7] bar7 is the last letter from the prev 5long that isn't bar1, bar3, bar4, bar6
# [bar2] bar2 is other 5long that doesn't have bar3 in it
# [bar6] val that 5long and o5long share that isn't bar1247
# [bar3] use 1 and bar6
# [bar5] is what's left

# def determine_config(test):
#     bar1 = ''
#     bar2 = ''
#     bar3 = ''
#     bar4 = ''
#     bar5 = ''
#     bar6 = ''
#     bar7 = ''

#     one = get_one(test)
#     seven = 


def get_all_output_values( data ):
    values = []
    for test, res in data:
        print(get_one(test))
    #     values.append( get_value(test, res) )

    # return values

def get_value(test, res):
    val = ""
    for v in output:
        print(v, get_digit(v))
        val += str(get_digit(v))

    return int(val)

def check_equality(digit, value):
    if len(digit) != len(value):
        return False
    true_count = 0
    for char in value:
        if char in digit:
            true_count += 1
    if true_count != len(digit):
        return False
    return True

def get_digit(digit):
    if len(digit) == 7:
        return '8'
    elif check_equality(digit,'cdfbe'):
        return '5'
    elif check_equality(digit,'gcdfa'):
        return '2'
    elif check_equality(digit,'fbcad'):
        return '3'
    elif len(digit) == 3:
        return '7'
    elif check_equality(digit,'cefabd'):
        return '9'
    elif check_equality(digit,'cdfgeb'):
        return '6'
    elif len(digit) == 4:
        return '4'
    elif check_equality(digit,'cagedb'):
        return '0'
    elif len(digit) == 1:
        return '1'



def main():
    f = open("day8_input.txt")
    # f = open("sample8.txt")
    data = load_data(f)

    print(count_unique(data))
    # print(sum(get_all_output_values(data)))
    get_all_output_values(data)

    
    return

if __name__ == "__main__": 
    main()