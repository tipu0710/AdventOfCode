import os

f = open(os.getcwd()+"/assets/day5.txt", "r")
input = f.read().split("\n")

max = 0

def getSeat(text):
    row = 0
    col = 0
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax  = 7
    for i in range(len(text)):
        if text[i] == "F":
            rowMax = int((rowMax+rowMin)/2.0)
            row = rowMax
        elif text[i] == "B":
            rowMin = int(round((rowMax+rowMin)/2.0))
            row = rowMin
        elif text[i] == "R":
            colMin = int(round((colMax+colMin)/2.0))
            col = colMin
        elif text[i] == "L":
            colMax = int((colMax+colMin)/2.0)
            col = colMax
    print(row, col)
    return (row * 8 + col)

for text in input:
    num = getSeat(text)
    if max < num:
        max = num

print(max)
    