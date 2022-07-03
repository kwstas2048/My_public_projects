import random
def sum_of_list(list):
    total = 0
    for val in list:
        total = total + val
    return total

class cell():
    def __init__(self, value=0, owner=0):
        self.value = value
        self.owner = owner
    def getvalue(self):
        return self.value
    def getowner(self):
        return self.owner
    def setvalue(self, value=0):
        self.value = value
    def setowner(self, owner=0):
        self.owner = owner

class Proximity_46(cell):
    def __init__(self, length_X=1, length_Y=1, pid=0):
        super().__init__()
        self.length_X = length_X
        self.length_Y = length_Y
        self.pid = pid
    def setpid(self, pid = 0):   # pid = player id 1: Κόκκινο, 2: Πράσινο
        if self.pid == 1:
            print("You choose Red player")
        elif self.pid == 2:
            print("You choose Green player")
        else:
            while self.pid not in [1, 2]:
                self.pid = int(input("Set player id 1 for Red and 2 for Green (red play first):"))
        return self.pid
    def setBoardSize(self , length_X = 1, length_Y = 1):
        while self.length_X % 2 != 0 or self.length_X <= 1:
            self.length_X = int(input("Give me 'an even' length of x dimention:"))
        while self.length_Y % 2 != 0 or self.length_Y <= 1:
            self.length_Y = int(input("Give me 'an even' length of y dimention:"))
        print("The board has", self.length_X, "row x", self.length_Y, "coloms")
        return self.length_X, self.length_Y
    def cellList(self, length_X, length_Y):
        self.cellList = []
        for j in range(length_X * length_Y):
            self.cellList.append([])
            _ = cell()     #          print("value of cell", j, "=", _.getvalue(), "\n", "owner of cell", j, "=", _.getowner())
            self.cellList[j] = _.getvalue(), _.getowner()
        return self.cellList
    def printboard(self, cellList, length_X, length_Y):
        print("_" * length_X * 30)
        for j in range(length_Y, 1, -2):
            for i in range(length_X):
                print("                cell<", cellList[(j - 1) * length_X + i][0], ",", cellList[(j - 1) * length_X + i][1], ">", end="")
            print("\n", "_" * length_X * 30)
            for i in range(length_X):
                print("cell<", cellList[(j - 2) * length_X + i][0], ",", cellList[(j - 2) * length_X + i][1], ">                ", end="")
            print("\n", "_" * length_X * 30)
    def findNeigthbours(self, pid, cellList, X, Y):
        self.list = cellList  # print(type(self.list))
        newlist = cellList  # print(type(newlist))
        for pos in range(X * Y):
            if self.list[pos][0] == 0: # value(pos)=0
                neigb = self.findMyNeigthbours(pos, X, Y)
                for obj in neigb:
                    if self.list[obj][0] != 0: # κατειλημμένος γείτονας
                        newlist[pos] = [0, pid]
        return newlist

    def placeTile(self, round, value, cellList, length_X, length_Y, pid):
        if round == 0:
            position = length_X * (length_Y - 1) / 2
        else:
            cellList_neigthbours = self.findNeigthbours(pid, cellList, length_X, length_Y)
            list = []
            for n in range(length_X * length_Y):
                list.append([])  # [[], [], ...,[]] n-times
                if cellList_neigthbours[n][0] == 0:  # Ελεύθερο κελί
                    neigb = self.findMyNeigthbours(n, length_X, length_Y)
                    for obj in neigb:  # [[], [], ...,[]] n-times * obj-times
                        nei_value = cellList_neigthbours[obj][0]
                        if value > nei_value:  # Κελί του αντιπάλου
                            list[n].append(nei_value)
                        elif cellList_neigthbours[obj][1] == pid:  # Δικό μου κελί
                            list[n].append(1)
                #   print("list", list)
            points = {n: sum(list[n]) for n in range(len(list))}
            print("points:", points)
            inverse = [(value, key) for key, value in points.items()]
            print("inverse", inverse)
            position = max(inverse)[1]
            print("Max score:", points[position])
            print("Position choosed by AI=", position)  # Ξέρω ότι δεν είναι AI
        return position

    def findMyNeigthbours(self, position, length_X, length_Y):                                                     # col:   0 | 1,...,X-2 | X-1  row:
        self.length_X = length_X                                                                                   #        10  |   11  |  12    Y-1  odd
        self.length_Y = length_Y                                                                                   #     7  |   8   |   9        Y-2  even
        if position == 0: # first cell (1)                                                                         #       ---  |  ---  |  ---    :
            return [1, self.length_X]   #2#                                                                        #    --- |  ---  |  ---        :
        elif position > 0 and position < self.length_X - 1: # rest in first row (2)                                #        4   |   5   |  6      1  odd
            return [position - 1, position + 1, position + self.length_X - 1, position + self.length_X]   #4#      #     1  |   2   |  3          0  even
        elif position == self.length_X - 1: # first row + last column (3)
            return [position - 1, position + self.length_X - 1, position + self.length_X]  #3#
        elif position == (self.length_Y - 1) * self.length_X: # last row + first column (10)
            return [position - self.length_X, position - self.length_X + 1, position + 1]  #3#
        elif position > self.length_X * (self.length_Y - 1) and position < self.length_X * self.length_Y - 1: # rest in last row (11)
            return [position - self.length_X, position - self.length_X + 1, position - 1, position + 1] #4#
        elif position == self.length_X * self.length_Y - 1: # last cell (12)
            return [position - self.length_X, position - 1] #2#
        elif (position // self.length_X) % 2 == 1:  # odd row (4) + (5) + (6)
            if position % length_X == 0: # first column (4)
                return [position - self.length_X, position - self.length_X + 1, position + 1, position + self.length_X, position + self.length_X + 1]
            elif position % length_X == length_X - 1: # last column (6)
                return [position - self.length_X, position - 1, position + self.length_X]  # 3#
            else: # central cells (5)
                return [position - self.length_X, position - self.length_X + 1, position - 1, position + 1, position + self.length_X, position + self.length_X + 1] #6#
        elif (position // self.length_X) % 2 == 0: # even row (7) + (8) + (9)
            if position % self.length_X == 0:  # first column (7)
                return [position - self.length_X, position + 1, position + self.length_X] #3#
            elif position % self.length_X == self.length_X - 1:  # last column (9)
                return [position - self.length_X - 1, position - self.length_X, position - 1, position + self.length_X - 1, position + self.length_X]  # 5#
            else: # central cells (8)
                return [position - self.length_X - 1, position - self.length_X, position - 1, position + 1, position + self.length_X - 1, position + self.length_X] #6#

    def applyChanges(self, cellList, position, value, pid, length_X, length_Y):
        cellList[int(position)] = [int(value), int(pid)]
        neigb = self.findMyNeigthbours(position, length_X, length_Y)
        for obj in neigb:
            if cellList[int(obj)][0] != 0  and cellList[int(obj)][1] == pid: # every neibgthbour cell that is mine +1 in value
                cellList[int(obj)][0] += 1
            else:
                if cellList[int(obj)][0] < value: # steal enemy's cells
                    v = cellList[int(obj)][0]
                    cellList[int(obj)] = [v, int(pid)]
        if pid == 1:        # 1: Κόκκινο, 2: Πράσινο
            newpid = 2
            print("Green player's turn")
        else:
            newpid = 1
            print("Red player's turn")
        return cellList, newpid

# Game start:
'''
# Είσοδος Μεταβλητών
X, Y, pid = 4, 6, 1
print("X=", X, "Y=", Y, "pid=", pid)
'''
game = Proximity_46()    # 1ος Γύρος length_X=X, length_Y=Y, pid=pid
pid = game.setpid()
X, Y = game.setBoardSize()
# Ορισμός αρχικής λίστας
cellList = []
for j in range(X * Y):
    cellList.append([])
    _ = cell()
    # print("value of c", j, "=", _.getvalue())
    # print("owner of c", j, "=", _.getowner())
    cellList[j].append(_.getvalue())
    cellList[j].append(_.getowner())

# cellList = game.cellList(X, Y)
# print("cellList:", cellList)
game.printboard(cellList, X, Y)

# Run the game:
for Round in range(X * Y):
    print("Round", Round + 1, ":")
    value = random.randrange(1, 21)
    print("The given value is:", value)
    if pid == 1:
        position = game.placeTile(Round, value, cellList, X, Y, pid)
    else:
        position = int(input("PlaceTile in position:"))
    cellList, pid = game.applyChanges(cellList, position, value, pid, X, Y)
#   print("cellList:", cellList)
    game.printboard(cellList, X, Y)
    neigthbours_of_position = game.findMyNeigthbours(position, X, Y)
    print("Neigthbours_of_position are:", neigthbours_of_position)
    if pid == 1:
        print("Red player's turn")
    elif pid == 2:
        print("Green player's turn")
print("The game has finish calculate the score:")