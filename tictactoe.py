class Grid:
  def __init__(self, length):
    self.grid = [[[0,0] for x in range(0,length)] for y in range(0,length)]

  def __len__(self):
    return len(self.grid)

  def __getitem__(self, key):
    return self.grid[key]

  def __str__(self):
    output, length = "", len(self.grid)
    for i in range(0, length):
      for j in range(0, length):
        if self.grid[i][j][0] == 1:
          output += "X"
        elif self.grid[i][j][1] == 1:
          output += "O"
        else:
          output += " "
        if j < length - 1:
          output += "|"
      if i < length - 1:
        output += "\n" + "--" * length  + "\n"
    return output

  def setGridBlock(self, x, y, value):
    if self.grid[x][y][1-value] == 0 and self.grid[x][y][value] == 0:
      self.grid[x][y][value] = 1
      self.grid[x][y][1-value] = 0
      return True
    return False

  def isWin(self, val):
    length = len(self.grid)
    for i in range(0,length):
      col = [self.grid[x][i] for x in range(0, length)]
      if self.checkRowCol(self.grid[i], val) or self.checkRowCol(col, val):
        return True
    firstDiagonal = [self.grid[x][x] for x in range(0, length)]
    secondDiagonal = [self.grid[length-1-x][x] for x in range(0,length)]
    if self.checkRowCol(firstDiagonal, val) or self.checkRowCol(secondDiagonal, val):
      return True
    return False

  def isStalemate(self):
    length = len(self.grid)
    firstDiagonal = [self.grid[x][x] for x in range(0, length)]
    secondDiagonal = [self.grid[length-1-x][x] for x in range(0,length)]
    for i in range(0,length):
      col = [self.grid[x][i] for x in range(0, length)]
      if self.checkStale(self.grid[i]) and self.checkStale(col) and self.checkStale(firstDiagonal) and self.checkStale(secondDiagonal):
        return True
    return False
  
  def checkStale(self, arr):
    numX, numO = 0, 0
    for i in range(0, len(arr)):
      if arr[i][0] == 1:
        numX += 1
      if arr[i][1] == 1:
        numO += 1
      if numX > 0 and numO > 0:
        return True
    return False
      
  def checkRowCol(self, arr, val):
    for i in range(0, len(arr)):
      if arr[i][val] == 0:
        return False
    return True


def playGame(length):
  board = Grid(length)
  player = 0
  while not board.isWin(0) and not board.isWin(1):
    print(board)
    print("Player " + str(player + 1) + " turn")
    changeCoordinates(board, player)
    if board.isWin(player):
      print("=====================================")
      print("Player" + str(player + 1) + " wins!")
      print("=====================================")
      print(board)
      return
    if board.isStalemate():
      print("=====================================")
      print("Stalemate!")
      print("=====================================")
      print(board)
      return
    player = 1 - player

def changeCoordinates(board, player):
  x,y = askCoordinates(board)
  while not board.setGridBlock(int(x),int(y),player):
    print("This move is not possible!")
    x,y = askCoordinates(board)
    board.setGridBlock(int(x),int(y),player)

def askCoordinates(board):
  x = int(input("Choose a x coordinate: "))
  while x < 0 or x >= len(board):
    print("Coordinate does not fit specified range of 0 to " + str(len(board)-1))
    x = int(input("Choose a x coordinate: "))
  y = int(input("Choose a y coordinate: "))
  while y < 0 or y >= len(board) :
    print("Coordinate does not fit specified range of 0 to " + str(len(board)-1))
    y = int(input("Choose a y coordinate: "))
  return x,y


playGame(3)
