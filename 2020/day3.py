import os

f = open(os.getcwd()+"/assets/day3.txt", "r")
text = f.read().split("\n")

position = 0
notFirst = False
treeCount = 0

for line in text:
    if line == "":
        continue
    if len(line) < position+1:
        lenth = len(line)
        i = int((position+1)/lenth)+1
        for x in range(i):
            line = line+line
            if len(line) >= position+1:
                break
    if notFirst:
        if line[position+1] == "#":
            treeCount += 1
        position += 3
    else:
        position += 2
        notFirst = True

print(treeCount)
