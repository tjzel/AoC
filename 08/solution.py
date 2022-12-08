def first_part():
    trees = []
    line = input()
    width = len(line)
    trees.append([])
    for l in line:
        trees[0].append([int(l), 0])
    length = 1
    while True:
        try: 
            line = input()
            trees.append([])
            for l in line:
                trees[length].append([int(l), 0])
            length += 1
        except: break
    sum = 0
    for i in range(0, length):
        maxHeight = -1
        for j in range(0, width):
            height = trees[i][j][0]
            if height > maxHeight:
                maxHeight = height
                if trees[i][j][1] == 0:
                    sum += 1
                    trees[i][j][1] = 1
                if maxHeight == 9: break

    for i in range(0, length):
        maxHeight = -1
        for j in range(width-1, -1, -1):
            height = trees[i][j][0]
            if height > maxHeight:
                maxHeight = height
                if trees[i][j][1] == 0:
                    sum += 1
                    trees[i][j][1] = 1
                if maxHeight == 9: break

    for i in range(0, width):
        maxHeight = -1
        for j in range(0, length):
            height = trees[j][i][0]
            if height > maxHeight:
                maxHeight = height
                if trees[j][i][1] == 0:
                    sum += 1
                    trees[j][i][1] = 1
                if maxHeight == 9: break

    for i in range(0, width):
        maxHeight = -1
        for j in range(length-1, -1, -1):
            height = trees[j][i][0]
            if height > maxHeight:
                maxHeight = height
                if trees[j][i][1] == 0:
                    sum += 1
                    trees[j][i][1] = 1
                if maxHeight == 9: break
    print(sum)

def second_part():
    trees = []
    line = input()
    width = len(line)
    trees.append([])
    for l in line:
        trees[0].append([int(l), 0])
    length = 1
    while True:
        try: 
            line = input()
            trees.append([])
            for l in line:
                trees[length].append([int(l), 0])
            length += 1
        except: break
    maxScore = 0

    for I in range(1, length-1):
        for J in range(1, length-1):
            right = 0
            left = 0
            down = 0
            up = 0
            maxHeight = trees[I][J][0]
            for j in range(J+1, width):
                height = trees[I][j][0]
                left += 1
                if height >= maxHeight: break

            for j in range(J-1, -1, -1):
                height = trees[I][j][0]
                right += 1
                if height >= maxHeight: break

            for i in range(I+1, length):
                height = trees[i][J][0]
                down += 1
                if height >= maxHeight: break

            for i in range(I-1, -1, -1):
                height = trees[i][J][0]
                up += 1
                if height >= maxHeight: break

            score = right * left * down * up
            if score > maxScore:
                maxScore = score
    print(maxScore)

second_part()