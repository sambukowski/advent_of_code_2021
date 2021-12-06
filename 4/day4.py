
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
                hit = ("x" if (self.data[i][j][1] == True) else "o")
                output += f"({self.data[i][j][0]:2.0f}, {hit}) "

            output += "]\n"
        output += "Is "
        if not self.check_winner():
            output += "not "
        output += "a winner.\n"
        # output += "\n"
        return output

    def check_winner(self):
        # check all rows
        hit_count = 0
        for i in range(0,5):
            for j in range(0,5):
                if (self.data[i][j][1] == True):
                    hit_count += 1
                if hit_count == 5:
                    return True
            hit_count = 0
        
        # check columns
        hit_count = 0
        for i in range(0,5):
            for j in range(0,5):
                if (self.data[j][i][1] == True):
                    hit_count += 1
                if hit_count == 5:
                    return True
            hit_count = 0

        # check diags 
        hit_count = 0
        for i in range(0,5):
            if (self.data[i][i][1] == True):
                hit_count += 1
        if hit_count == 5:
            return True
        hit_count = 0

        for i in range(0,5):
            if (self.data[i][4-i][1] == True):
                hit_count += 1
        if hit_count == 5:
            return True
        hit_count = 0

        # else the board hast won yet
        return False

    def get_winning_score(self, val):
        if self.check_winner():
            score = 0
            for i in range(0,5):
                for j in range(0,5):
                    if self.data[i][j][1] == False:
                        score += self.data[i][j][0]

            return (score * val), score
        else:
            return None

    def mark_number(self, number):
        for i in range(0,5):
            for j in range(0,5):
                if self.data[i][j][0] == number and self.data[i][j][1] == False:
                    self.data[i][j][1] = True
        return 

    def calculate_win(self, inputs):
        number_of_moves_needed = 0
        winning_val = None
        winning_score = None

        for val in inputs:
            self.mark_number( val )
            number_of_moves_needed += 1
            if self.check_winner() == True:
                winning_val = val
                winning_score = self.get_winning_score( val )
                break

        self.number_of_moves_needed = number_of_moves_needed
        self.winning_val = winning_val
        self.winning_score = winning_score

def main():
    f = open("day4_input.txt")
    strings = f.readlines()

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

    for board in boards:
        board.calculate_win( inputs )


    # part 1
    first_winner = boards[0]
    for board in boards:
        if board.number_of_moves_needed < first_winner.number_of_moves_needed:
            first_winner = board

    print(f"moves to first win: {first_winner.number_of_moves_needed}")
    print(f"day4 part 1: {first_winner.winning_score[0]}")

    moves_needed = 0
    last_winner = None
    for board in boards:
        if board.number_of_moves_needed > moves_needed:
            moves_needed = board.number_of_moves_needed
            last_winner = board

    print(f"moves to last win: {last_winner.number_of_moves_needed}")
    print(f"day4 part 2: {last_winner.winning_score[0]}")

    return


if __name__ == "__main__": 
    main()