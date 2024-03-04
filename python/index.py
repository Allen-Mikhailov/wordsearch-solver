boardf = open("./puzzleboard.txt", "r")
wordsf = open("./words.txt", "r")

boardLines = boardf.read().split("\n")
board = []
for line in boardLines:
    board.append([*line.lower()])
words = wordsf.read().split("\n")

width = len(board[0])
height = len(board)

directions = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1]
]

def validCheck(word, dir, x, y):
    for c in word:
        # print(x, y, len(board), len(board[y]))
        if (c != board[y][x]):
            return False
        
        x += dir[0]
        y += dir[1]
        if (x >= width or x < 0 or y >= height or y < 0):
            return False
        pass
    return True

def checkCharacter(x, y):
    for dir in directions:
        for word in words:
            if (validCheck(word, dir, x, y)):
                print(word+" found at "+str(x)+", "+str(y)+" in dir "+str(dir))

for x in range(width):
    for y in range(height):
        checkCharacter(x, y)