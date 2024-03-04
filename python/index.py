boardf = open("./puzzleboard.txt", "r")
wordsf = open("./words.txt", "r")

boardLines = boardf.read().split("\n")
board = []
for line in boardLines:
    board.append([*line.lower()])
words = wordsf.read().split("\n")
foundWords = {}
for word in words:
    foundWords[word] = False

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
                foundWords[word] = True
                print(word+" found at "+str(x)+", "+str(y)+" in dir "+str(dir))

for x in range(width):
    for y in range(height):
        checkCharacter(x, y)

foundCount = 0
for word in words:
    print(word+" "+ ("found" if foundWords[word] else "not found"))
    if (foundWords[word]):
        foundCount += 1
print('Found '+str(foundCount) + " of "+str(len(words)) + " words")

string = ""
for word in words:
    string+=word+","
print(string)