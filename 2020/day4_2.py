import os
import ast
import re

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

def byrValidate(yearTxt):
    if len(yearTxt) != 4:
        return False
    year = int(yearTxt)
    if year >= 1920 and year <= 2002:
        return True
    else:
        return False

def iyrValidate(yearTxt):
    if len(yearTxt) != 4:
        return False
    year = int(yearTxt)
    if year >= 2010 and year <= 2020:
        return True
    else:
        return False

def eyrValidate(yearTxt):
    if len(yearTxt) != 4:
        return False
    year = int(yearTxt)
    if year >= 2010 and year <= 2030:
        return True
    else:
        return False

def hgtValidate(hgt):
    type = hgt[-2:]
    if type != "in":
        if type != "cm":
            return False
    num = int(hgt.split(type)[0])
    if type == "cm":
        if num >= 150 and num <= 193:
            return True
        else: 
            return False
    elif type == "in":
        if num >= 59 and num <= 76:
            return True
        else:
            return False
    else:
        return False

def hclValidate(hcl):
    if hcl[0] != "#" or len(hcl) != 7:
        return False
    color = hcl.split("#")[1]
    slower=''.join(re.findall(r'[a-f]',color))
    num = ''.join(re.findall(r'[0-9]',color))

    if len(slower) + len(num) == 6:
        return True
    else:
        return False

    
def eclValidate(text):
    find = False
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for pp in ecl:
        result = text.find(pp)
        if result >= 0:
            find = True
            break
    return find

def pidValidate(pid):
    if len(pid) == 9:
        return True
    else:
        return False
    
        

def validate(text):
    valid = False
    valid = byrValidate(text['byr'])
    if valid != True:
        return valid
    valid = iyrValidate(text['iyr'])
    if valid != True:
        return valid
    valid = eyrValidate(text['eyr'])
    if valid != True:
        return valid
    valid = hgtValidate(text['hgt'])
    if valid != True:
        return valid
    valid = hclValidate(text['hcl'])
    if valid != True:
        return valid
    valid = eclValidate(text['ecl'])
    if valid != True:
        return valid
    valid = pidValidate(text['pid'])
    
    return valid


for data in text:
    splitedData = data.split("\n")
    passText = {}
    mainText = ""
    for sd in splitedData:
        finalList = sd.split(" ")
        for final in finalList:
            ls = final.split(":")
            passText[ls[0]] = ls[1]
            mainText = mainText +" "+ ls[0]

    if check(mainText) and validate(passText):
        count += 1

print(count)