def first_part():
    line = input()
    for i in range (0, len(line)-3):
        subLine = line[i:i+4]
        #print(subLine)
        setLine = set(subLine)
        #print(setLine)
        if(len(setLine) == 4):
            print(i+4)
            break

def second_part():
    line = input()
    for i in range (0, len(line)-13):
        subLine = line[i:i+14]
        #print(subLine)
        setLine = set(subLine)
        #print(setLine)
        if(len(setLine) == 14):
            print(i+14)
            break

second_part()