import os

f = open(os.getcwd()+"/2019/assets/day1.txt", "r")

text = f.read().split("\n")

num = []

totalAmmount = 0

for i in range(0, len(text)): 
    if text[i] == "":
        continue
    num.append(int(text[i]))

for fuel in num:
    finalFuel = int(fuel/3)-2
    totalAmmount += finalFuel

print(totalAmmount)