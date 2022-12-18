def first_part():
    cycle = 1
    register = 1
    cycleTarget = 20
    cycleDiff = 40
    cycleEnd = 220
    sum = 0

    while True:
        if cycle == cycleTarget:
            sum += register * cycle
            if cycleTarget == cycleEnd:
                break
            cycleTarget += cycleDiff
        try:
            line = input().split(" ")
        except:
            break
        if len(line) > 1:
            cycle += 1
            if cycle == cycleTarget:
                sum += register * cycle
                if cycleTarget == cycleEnd:
                    break
                cycleTarget += cycleDiff
            register += int(line[1])
        cycle += 1

    print(sum)

def second_part():
    register = 1
    width = 40
    pixel = 0

    while True:
        if pixel == width:
            print()
            pixel = 0
        if register-1 <= pixel and pixel <= register+1:
            print("#", end="")
        else:
            print(".", end="")
        try:
            line = input().split(" ")
        except:
            break
        if len(line) > 1:
            pixel += 1
            if pixel == width:
                print()
                pixel = 0
            if register-1 <= pixel and pixel <= register+1:
                print("#", end="")
            else:
                print(".", end="")
            register += int(line[1])
        pixel += 1

#first_part()
second_part()