def first_part():
    counter = 0
    while True:
        try:
            line = input()
        except:
            break
        rangeList = line.split(',')
        leftRange = rangeList[0].split('-')
        rightRange = rangeList[1].split('-')
        if int(leftRange[0]) < int(rightRange[0]):
            if int(rightRange[1]) <= int(leftRange[1]): 
                counter+=1
        elif int(leftRange[1]) <= int(rightRange[1]) or leftRange[0] == rightRange[0]: 
            counter +=1
    print(counter)

def second_part():
    counter = 0
    while True:
        try:
            line = input()
        except:
            break
        rangeList = line.split(',')
        leftRange = rangeList[0].split('-')
        rightRange = rangeList[1].split('-')
        if int(leftRange[0]) >= int(rightRange[0]) and int(leftRange[0]) <= int(rightRange[1]): counter +=1
        elif int(rightRange[0]) >= int(leftRange[0]) and int(rightRange[0]) <= int(leftRange[1]): counter +=1
    print(counter)

second_part()