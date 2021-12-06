class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

class VentLine:
    def __init__(self,data):
        vals = data.split(" -> ")
        tmp = vals[0].split(',')
        self.p1 = Point(tmp[0],tmp[1])
        tmp = vals[1].split(',')
        self.p2 = Point(tmp[0],tmp[1])

        self.horizontal = (True if self.p1.y == self.p2.y else False)
        self.vertical   = (True if self.p1.x == self.p2.x else False)
        self.diagonal   = (True if (abs(self.p1.x-self.p2.x) == abs(self.p1.y-self.p2.y)) else False)
        self.is_point   = (True if (self.p1.x == self.p2.x and self.p1.y == self.p2.y and self.p1.x == self.p1.y) else False)

        # print(self)

    def __str__(self):
        line_type = None
        if self.horizontal:
            line_type = "horz"
        elif self.vertical:
            line_type = "vert"
        elif self.diagonal:
            line_type = "diag"
        elif self.is_point:
            line_type = "point"

        x_path, y_path = self.get_line_path()

        output = f"{line_type}: x({self.p1.x},{self.p1.y}), y({self.p2.x},{self.p2.y})\n"
        output += f"\tx: {x_path}\n"
        output += f"\ty: {y_path}"
        return output

    def get_line_path(self, vh_only=False):
        if self.vertical:
            return self.get_vertical_line()
        elif self.horizontal:
            return self.get_horizontal_line()
        elif not vh_only and self.diagonal:
            return self.get_diagonal_line()
        elif self.is_point:
            return [self.p1.x], [self.p1.y]
        else:
            return []

    def get_vertical_line(self):
        y_list = list(range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y)+1))
        if not y_list:
            y_list = [self.p1.y]
        return [self.p1.x], y_list

    def get_horizontal_line(self):
        x_list = list(range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x)+1))
        if not x_list:
            x_list = [self.p1.x]
        return x_list, [self.p1.y]

    def get_diagonal_line(self):
        x_slope = (1 if (self.p2.x-self.p1.x > 0) else -1)
        y_slope = (1 if (self.p2.y-self.p1.y > 0) else -1)
        x_list = list(range(self.p1.x, self.p2.x+x_slope, x_slope))
        y_list = list(range(self.p1.y, self.p2.y+y_slope, y_slope))
        if not x_list:
            x_list = [self.p1.x]
        if not y_list:
            y_list = [self.p1.y]

        return x_list, y_list

        

class Ventscape:
    def __init__(self, ventlines, vh_only=False):
        self.x_max = max([ max(p.p1.x, p.p2.x) for p in ventlines ]) + 1
        self.y_max = max([ max(p.p1.x, p.p2.y) for p in ventlines ]) + 1

        self.data = []
        for i in range(0,self.y_max):
            tmp_list = []
            for j in range(0,self.x_max):
                tmp_list.append(0)
            self.data.append(tmp_list)

        for line in ventlines:
            self.add_line( line, vh_only=vh_only )

    def __str__(self):
        output = ""
        for row in self.data:
            for item in row:
                output += str(item)
            output += "\n"
        output += f"size: {self.x_max}, {self.y_max}"
        
        return output

    def add_line(self, line, vh_only=False):
        # this function is a nightmare...
        line_path = line.get_line_path(vh_only=vh_only)
        if not line_path:
            return False
        else:
            x_list, y_list = line_path[0], line_path[1]
            if line.horizontal or line.vertical:
                for y in y_list:
                    for x in x_list:
                        self.data[y][x] += 1
            else:
                diag_list = zip(x_list,y_list)
                for pair in diag_list:
                    self.data[pair[1]][pair[0]] += 1

            return True


    def get_dangerous_count(self, thresh=2):
        count = 0
        for row in self.data:
            for item in row:
                if item >= thresh:
                    count += 1
        
        return count

def main():
    f = open("day5_input.txt")
    # f = open("sample5.txt")
    strings = f.readlines()
    ventlines = [VentLine(line) for line in strings ]

    ventscape_p1 = Ventscape( ventlines, vh_only=True ) # part 1
    ventscape_p2 = Ventscape( ventlines )               # part 2
    # print(ventscape_p1)
    print(f"Day 5, part 1: There are {ventscape_p1.get_dangerous_count()} dangerous spots.")

    # print(ventscape_p2)
    print(f"Day 5, part 2: There are {ventscape_p2.get_dangerous_count()} dangerous sponts.")

    return

if __name__ == "__main__": 
    main()