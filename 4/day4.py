
class BingoBoard:
    def __init__(self,rows):
        self.data = []

        for i in range(0,5):
            r = []
            for j in range(0,5):
                r.append( [rows[i][j],False] )
            self.data.append(r)

        # print(self.data)
        # print()

    def __str__(self):
        output = ""
        for i in range(0,5):
            output += "[ "
            for j in range(0,5):
                hit = ("x" if self.data[i][j][1] == True else "o")
                output += f"({self.data[i][j][0]:2.0f}, {hit}) "

            output += "]\n"
        output += "\n"
        return output

    def check_winner(self):
        # check all rows
        hit_count = 0
        for i in range(0,5):
            for j in range(0,5):
                if self.data[i][j][1] == True:
                    hit_count += 1
                if hit_count == 5:
                    return True
        
        # check columns
        hit_count = 0
        for i in range(0,5):
            for j in range(0,5):
                if self.data[j][i][1] == True:
                    hit_count += 1
                if hit_count == 5:
                    return True

        # check diags 
        hit_count = 0
        for i in range(0,5):
            if self.data[i][i][1] == True:
                hit_count += 1
            if hit_count == 5:
                return True

        for i in range(0,5):
            if self.data[i][4-i][1] == True:
                hit_count += 1
            if hit_count == 5:
                return True

        # else the board hast won yet
        return False

    def get_winning_score(self, val):
        if self.check_winner():
            score = 0
            for i in range(0,5):
                for j in range(0,5):
                    if self.data[i][j][1] == False:
                        score += self.data[i][j][0]

            return (score * val)
        else:
            return None

    def mark_number(self, number):
        for i in range(0,5):
            for j in range(0,5):
                if self.data[i][j][0] == number:
                    self.data[i][j][1] = True
        return 

def main():
    f = open("day4_input.txt")
    strings = f.readlines()

    # === part 1 ===

    inputs = [int(x) for x in strings[0].split(',')]
    boards = []

    tmp_brd = []
    for i in range(2,len(strings)):
        if len(strings[i].split()) > 3: 
            tmp_brd.append([int(x) for x in strings[i].split()])
        else:
            if len(tmp_brd) == 5:
                boards.append( BingoBoard( tmp_brd.copy() ) )
                tmp_brd = []

    # print(len(boards))
    # print(boards[0])

    winning_score = 0
    for val in inputs:
        for board in boards:
            board.mark_number( val )
            if board.check_winner() == True:
                print(board)

                winning_score = board.get_winning_score( val )
                break

    print(f"day4 part 1: {winning_score}")

    # === part 2 ===

    return


if __name__ == "__main__": 
    main()