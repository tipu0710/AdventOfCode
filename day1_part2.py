f = open("assets/input.txt", "r")
text = f.read().split("\n")

num = []

for i in range(0, len(text)): 
    if text[i] == "":
        continue
    num.append(int(text[i]))

for x in num:
    for y in num:
        for z in num:
            if x + y + z == 2020:
                print(str(x*y*z))