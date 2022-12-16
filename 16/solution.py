class Valve:
    def __init__(self, number, label, flowRate, directionList):
        self.number = number
        self.label = label
        self.flowRate = flowRate
        self.directionList = directionList

    def setDirections(self, valveDict):
        for i in range(len(self.directionList)):
            label = self.directionList[i].label
            self.directionList[i] = valveDict.get(label)
    
def first_part():
    valveList = list()
    valveDict = dict()
    i = 0
    while True:
        try:
            line = input().split(" ")
        except:
            break
        number = i
        label = line[0]
        flowRate = line[1]
        directionList = line[2:]
        valve = Valve(number, label, flowRate, directionList)
        valveDict[label]=valve
        #valveDict.get
        valveList.append(valve)
        i += 1
    for v in valveList:
        v.setDirections(valveDict)

    
first_part()
