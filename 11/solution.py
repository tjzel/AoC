import math

class Monkey:
    modulo = 1
    def __init__(self, id, throwList, operation, operationValue, condition, trueTarget, falseTarget):
        self.id = id
        self.throwList = throwList
        self.operation = operation
        self.operationValue = operationValue
        self.condition = condition
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.inspections = 0

    def makeTurn(self, monkeys, divisor):
        #print("[", end=" ")
        #for m in monkeys:
        #    print (m.id, end = " ")
        #print("]")
        #print("Monkey:", self.id, self.throwList)
        while len(self.throwList) > 0:
            t = self.throwList.pop()
            self.inspections += 1
            level = self.operation(t, self.operationValue)
            if divisor != None:
                level = level//3
            else:
                level = level % Monkey.modulo
            if level % self.condition == 0:
                catcher = monkeys[self.trueTarget]
            else:
                catcher = monkeys[self.falseTarget]
            catcher.catch(level)

    def catch(self, level):
        self.throwList.append(level)

def adding(level, value):
    if value == None:
        value = level
    return level + value

def mulitplying(level, value):
    if value == None:
        value = level
    return level * value

def first_part():
    monkeys = list()
    i = 0
    while True:
        try:
            #print("i: ", i)
            line = input()
            if len(line) == 0:
                line = input()
            id = int(line)
            temp = input().split(" ")
            throwList = list()
            for t in temp:
                throwList.append(int(t))
            temp = input().split(" ")
            operation = temp[0]
            if operation == "+":
                operation = adding
            else:
                operation = mulitplying
            if len(temp) > 1:
                operationValue = int(temp[1])
            else:
                operationValue = None
            condition = int(input())
            trueTarget = int(input())
            falseTarget = int(input())
        except:
            #print (id, throwList, operation, operationValue, condition, trueTarget, falseTarget)
            break
        monkeys.append(Monkey(id,throwList,operation, operationValue, condition, trueTarget, falseTarget))
        i+=1
    Monkey.modulo = monkeys[0].condition
    for m in monkeys:
        Monkey.modulo = math.lcm(Monkey.modulo, m.condition)
    print(Monkey.modulo)
    #print(len(monkeys))
    for i in range(20):
        for m in monkeys:
            m.makeTurn(monkeys, 3)
        i += 1
    inspections = list()
    for m in monkeys:
        inspections.append(m.inspections)
    inspections.sort(reverse=True)
    #print(inspections[0], inspections[1])
    print(inspections[0]*inspections[1])

def second_part():
    monkeys = list()
    i = 0
    while True:
        try:
            line = input()
            if len(line) == 0:
                line = input()
            id = int(line)
            temp = input().split(" ")
            throwList = list()
            for t in temp:
                throwList.append(int(t))
            temp = input().split(" ")
            operation = temp[0]
            if operation == "+":
                operation = adding
            else:
                operation = mulitplying
            if len(temp) > 1:
                operationValue = int(temp[1])
            else:
                operationValue = None
            condition = int(input())
            trueTarget = int(input())
            falseTarget = int(input())
        except:
            break
        monkeys.append(Monkey(id,throwList,operation, operationValue, condition, trueTarget, falseTarget))
        i+=1
    Monkey.modulo = monkeys[0].condition
    for m in monkeys:
        Monkey.modulo = math.lcm(Monkey.modulo, m.condition)
    for i in range(10000):
        for m in monkeys:
            m.makeTurn(monkeys, None)
        i += 1
    inspections = list()
    for m in monkeys:
        inspections.append(m.inspections)
    inspections.sort(reverse=True)
    print(inspections[0]*inspections[1])

#first_part()
second_part()
        
    

