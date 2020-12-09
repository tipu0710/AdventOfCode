import os
import ast

f = open(os.getcwd()+"/assets/day4.txt", "r")
text = f.read().split("\n\n")

checkList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0

def check(text):
    find = True
    for pp in checkList:
        result = text.find(pp)
        if result == -1:
            find = False
            break
    return find


for data in text:
    splitedData = data.split("\n")
    passText = ""
    for sd in splitedData:
        finalList = sd.split(" ")
        for final in finalList:
            passText = passText +" "+ final.split(":")[0]
    if check(passText):
        count += 1
    

print(count)            
