import os

f = open(os.getcwd()+"/assets/day3.txt", "r")
text = f.read().split("\n")[:-1]
print(text)
def getTree(data, right, down):
    steps = len(data)
    width = len(data[0])
    count = 0
    curStep = 0
    while curStep < steps - down:
        y = curStep + down
        x = ((y / down) * right) % width
        if (data[y][x]) == "#":
            count += 1
        curStep += down
    return count

print(getTree(text, 1, 1))
print(getTree(text,3, 1))
print(getTree(text,5, 1))
print(getTree(text,7, 1))
print(getTree(text,1, 2))
print(getTree(text,1, 1)*getTree(text,3, 1)*getTree(text,5, 1)*getTree(text,7, 1)*getTree(text,1, 2))
