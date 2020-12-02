f = open("assets/day2.txt", "r")
text = f.read().split("\n")

correctPass = 0
count = 0

for passPolicy in text:
    if passPolicy == "":
        continue
    pp = passPolicy.split(":")
    policy = pp[0]
    password = pp[1].replace(" ", "")

    policySplit = policy.split(" ")
    letter = policySplit[1]

    numList = policySplit[0].split("-")

    minNum = int(numList[0])
    maxNum = int(numList[1])

    numOfAppear = password.count(letter)

    if numOfAppear>= minNum and numOfAppear <= maxNum:
        correctPass += 1
    count += 1

print(str(correctPass))
print(count)



