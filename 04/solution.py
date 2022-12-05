import re
list = []
line = input()
#normalizedLine = re.sub("", "[[]]", line)
normalizedLine = re.sub("    ", " -", line)
splitLine = normalizedLine.split(" ")
for s in splitLine:
    list.append([])

while True:
    i = 0
    for s in splitLine:
        if(s != "-"):
            list[i].append(s)
        i+=1
    try:
        line = input()
    except:
        break
    if line == "": break
    #normalizedLine = re.sub("", "[", line)
    normalizedLine = re.sub("    ", " -", line)
    splitLine = normalizedLine.split(" ")
    print(normalizedLine)