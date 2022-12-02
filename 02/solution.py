import sys

def first_part():
    score = 0
    while True:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        if line == "": break
        else:
            values = line.split(' ')
            if values[0] == "A":
                if values[1] == "X":
                    score += 4
                if values[1] == "Y":
                    score += 8
                if values[1] == "Z":
                    score += 3
            if values[0] == 'B':
                if values[1] == 'X':
                    score += 1
                if values[1] == 'Y':
                    score += 5
                if values[1] == 'Z':
                    score += 9
            if values[0] == 'C':
                if values[1] == 'X':
                    score += 7
                if values[1] == 'Y':
                    score += 2
                if values[1] == 'Z':
                    score += 6
    print(score)

def second_part():
    score = 0
    while True:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        if line == "": break
        else:
            values = line.split(' ')
            if values[0] == "A":
                if values[1] == "X":
                    score += 3
                if values[1] == "Y":
                    score += 4
                if values[1] == "Z":
                    score += 8
            if values[0] == 'B':
                if values[1] == 'X':
                    score += 1
                if values[1] == 'Y':
                    score += 5
                if values[1] == 'Z':
                    score += 9
            if values[0] == 'C':
                if values[1] == 'X':
                    score += 2
                if values[1] == 'Y':
                    score += 6
                if values[1] == 'Z':
                    score += 7
    print(score)

second_part()