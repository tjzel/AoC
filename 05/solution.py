import re
def first_part():
    list = []
    line = input()
    splitLine = line.split(" ")
    for s in splitLine:
        list.append([])

    while True:
        i = 0
        for s in splitLine:
            if(s != "-"):
                list[i].insert(0, s)
            i+=1
        try:
            line = input()
        except:
            break
        if bool(re.match('[1-9]', line)): break
        splitLine = line.split(" ")

    line = input()

    while True:
        try:
            line = input()
        except:
            break
        splitLine = line.split(" ")
        amount = int(splitLine[0])
        fromStack = int(splitLine[1]) - 1
        toStack = int(splitLine[2]) - 1
        for i in range(0, amount):
            list[toStack].append(list[fromStack].pop())
    for l in list:
        print(l[-1], end="")
    print()

def second_part():
    list = []
    line = input()
    splitLine = line.split(" ")
    for s in splitLine:
        list.append([])

    while True:
        i = 0
        for s in splitLine:
            if(s != "-"):
                list[i].insert(0, s)
            i+=1
        try:
            line = input()
        except:
            break
        if bool(re.match('[1-9]', line)): break
        splitLine = line.split(" ")

    line = input()

    while True:
        try:
            line = input()
        except:
            break
        splitLine = line.split(" ")
        amount = int(splitLine[0])
        fromStack = int(splitLine[1]) - 1
        toStack = int(splitLine[2]) - 1
        for i in range(-amount, 0, 1):
            list[toStack].append(list[fromStack].pop(i))
    for l in list:
        print(l[-1], end="")
    print()

second_part()
