def first_part():
    sum = 0
    breakFlag = False
    while True:
        try:
            line = input()
        except:
            break
        for i in range (0, len(line)//2):
            for j in range (len(line)//2, len(line)):
                if line[i] == line[j]:
                    if line[i].islower(): sum += ord(line[i]) - ord('a') + 1
                    else : sum += ord(line[i]) - ord('A') + 27
                    breakFlag = True
                    break
            if breakFlag:
                breakFlag = False
                break
    print(sum)

def second_part():
    sum = 0
    while True:
        try:
            set1 = set(input())
            set2 = set(input())
            set3 = set(input())
        except:
            break
        for char in (set1.intersection(set2.intersection(set3))): break
        if char.islower(): sum += ord(char) - ord('a') + 1
        else: sum += ord(char) - ord('A') + 27
    print(sum)

second_part()