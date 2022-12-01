import sys

max = 0
temp = 0
calories = []
while True :
    line = sys.stdin.readline()
    if line == "":
        calories.append(temp)
        break
    elif line == "\n":
        calories.append(temp)
        temp = 0
    else:
        temp += int(line)
    #print(temp)
calories.sort(reverse=True)
print(calories[0])
print(calories[0] + calories[1] + calories[2])
