import os

f = open(os.getcwd()+"/2020/assets/day2.txt", "r")
text = f.read().split("\n")

correctPass = 0
count = 0

test = "hjdgfhjbjh"

for passPolicy in text:
    if passPolicy == "":
        continue
    pp = passPolicy.split(":")
    policy = pp[0]
    password = pp[1].replace(" ", "")

    policySplit = policy.split(" ")
    letter = policySplit[1]

    numList = policySplit[0].split("-")

    firstnum = int(numList[0])
    lastNum = int(numList[1])

    if password[firstnum-1] == letter and password[lastNum-1] != letter:
        correctPass += 1
    elif password[firstnum-1] != letter and password[lastNum-1] == letter:
        correctPass += 1
    
    count += 1

print(correctPass)
print(count)



