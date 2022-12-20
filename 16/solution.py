import queue

class OpenedValvesSet:
    def __init__(self):
        self.info = 0
        self.length = 0
    def add(self, valve):
        self.info = self.info | 1 << valve.number
        self.length += 1
    def remove(self, valve):
        self.info = self.info & ~(1 << valve.number)
        self.length -= 1
    def contains(self, valve):
        if self.info & 1 << valve.number:
            return True
        return False

class Cave:
    def __init__(self, valveList, startingValve):
        self.valveList = valveList
        self.realValveList = list()
        self.startingValve = startingValve
        self.realValveList.append(startingValve)
        self.soloMemory = dict()
        self.friendMemory = dict()
        for v in valveList:
            if v.flowRate > 0:
                self.realValveList.append(v)
        self.realValveAmount = len(self.realValveList)-1
        for R in self.realValveList:
            for r in self.realValveList:
                if R != r:
                    R.neighbourList.append(r)

    def makePaths(self):
        for i in range(len(self.realValveList)-1):
            start = self.realValveList[i]
            while len(start.neighbourList) > 0:
                end = start.neighbourList[0]
                self.findPath(start, end)

    def findPath(self, start, end):
        valveQueue = queue.PriorityQueue()
        start.visited = True
        distance = len(self.valveList)
        paths = list()
        queueLength = 0
        for d in start.directionList:
            valveQueue.put((1, d, list()))
            d.visited = True
            queueLength += 1
        while queueLength > 0:
            temp = valveQueue.get()
            queueLength -= 1
            length = temp[0]
            valve = temp[1]
            path = temp[2]
            if length > distance:
                break
            if valve == end:
                distance = length
                paths.append(path)
            else:
                for d in valve.directionList:
                    if d.visited == False:
                        d.visited = True
                        valveQueue.put((length+1, d, path + [valve]))
                        queueLength += 1

        for v in self.valveList:
            v.visited = False

        start.neighbourList.remove(end)
        end.neighbourList.remove(start)

        for P in paths:
            for p in P:
                if p in self.realValveList:
                    return

        path = paths[0]
        if len(path) > 0:
            returnPath = reversed(path)
        else:
            returnPath = list()
        start.neighbours.append((distance, end, path))
        end.neighbours.append((distance, start, returnPath))

    def soloMemoryAccess(self, start, prev, radius, openedValves):
        result = self.soloMemory.get((start, prev, radius, openedValves.info))
        if result == None:
            result = self.findBestRoute(start, prev, radius, openedValves)
            self.soloMemory[(start, prev, radius, openedValves.info)] = result
        return result

    def friendMemoryAccess(self, args, radius, openedValves):
        humanArgs = args[0]
        friendArgs = args[1]
        humanStart = humanArgs[0]
        humanRadius = humanArgs[2]
        friendStart = friendArgs[0]
        friendRadius = friendArgs[2]
        result = self.friendMemory.get((humanStart, humanRadius, friendStart, friendRadius, radius, openedValves.info))
        if result == None:
            humanNew = (humanStart, humanStart, humanRadius)
            friendNew = (friendStart, friendStart, friendRadius)
            argsNew = (humanNew, friendNew)
            result = self.findBestRouteWithFriend(argsNew, radius, openedValves)
            self.friendMemory[(humanStart, humanRadius, friendStart, friendRadius, radius, openedValves.info)] = result
        return result

    def findBestRoute(self, start, prev, radius, openedValves):
        if openedValves.length == self.realValveAmount: 
            return 0
        maxPressure = 0
        # NOT OPENING
        for n in start.neighbours:
            valve = n[1]
            distance = n[0]
            if radius - distance > 1 and valve != prev:
               result = self.soloMemoryAccess(valve, start, radius - distance, openedValves) 
               maxPressure = max(maxPressure, result)
        # OPENING
        if start.flowRate > 0 and not openedValves.contains(start):
            radius -= 1
            pressure = start.flowRate * radius
            maxPressure = max(maxPressure, pressure)
            openedValves.add(start)
            for n in start.neighbours:
                valve = n[1]
                distance = n[0]
                if radius - distance > 1:
                    result = self.soloMemoryAccess(valve, start, radius - distance, openedValves)
                    maxPressure = max(maxPressure, pressure + result)
            openedValves.remove(start)
        return maxPressure

    def findBestRouteWithFriend(self, args, radius, openedValves):
        if radius == 0 or openedValves.length == self.realValveAmount:
            return 0
        humanArgs = args[0]
        friendArgs = args[1]
        humanStart = humanArgs[0]
        humanPrev = humanArgs[1]
        humanRadius = humanArgs[2]
        friendStart = friendArgs[0]
        friendPrev = friendArgs[1]
        friendRadius = friendArgs[2]
        maxPressure = 0
        if radius == humanRadius:
            # HUMAN AND FRIEND
            if radius == friendRadius:
                # SOLO HUMAN
                if friendStart.flowRate > 0 and not openedValves.contains(friendStart):
                    friendPressure = friendStart.flowRate * (friendRadius - 1)
                    openedValves.add(friendStart)
                    soloHumanPressure = self.soloMemoryAccess(humanStart, humanPrev, humanRadius, openedValves)
                    maxPressure = max(maxPressure, friendPressure + soloHumanPressure)
                    openedValves.remove(friendStart)
                else:
                    soloHumanPressure = self.soloMemoryAccess(humanStart, humanPrev, humanRadius, openedValves)
                    maxPressure = max(maxPressure, soloHumanPressure)
                # SOLO FRIEND
                if humanStart.flowRate > 0 and not openedValves.contains(humanStart):
                    humanPressure = humanStart.flowRate * (humanRadius - 1)
                    openedValves.add(humanStart)
                    soloFriendPressure = self.soloMemoryAccess(friendStart, friendPrev, friendRadius, openedValves)
                    maxPressure = max(maxPressure, humanPressure + soloFriendPressure)
                    openedValves.remove(humanStart)
                else:
                    soloFriendPressure = self.soloMemoryAccess(friendStart, friendPrev, friendRadius, openedValves)
                    maxPressure = max(maxPressure, soloFriendPressure)
                # HUMAN NOT OPENING
                for humanNeighbour in humanStart.neighbours:
                    humanValve = humanNeighbour[1]
                    humanDistance = humanNeighbour[0]
                    if humanRadius - humanDistance > 1 and humanValve != humanPrev:
                        humanNew = (humanValve, humanStart, humanRadius - humanDistance)
                        # FRIEND NOT OPENING
                        for friendNeighbour in friendStart.neighbours:
                            friendValve = friendNeighbour[1]
                            friendDistance = friendNeighbour[0]
                            if friendRadius - friendDistance > 1 and friendValve != friendPrev:
                                friendNew = (friendValve, friendStart, friendRadius - friendDistance)
                                argsNew = (humanNew, friendNew)
                                radiusNew = max(argsNew[0][2], argsNew[1][2])
                                result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                                maxPressure = max(maxPressure, result)
                        # FRIEND OPENING
                        if friendStart.flowRate > 0 and not openedValves.contains(friendStart):
                            friendPressure = friendStart.flowRate * (friendRadius - 1)
                            openedValves.add(friendStart)
                            for friendNeighbour in friendStart.neighbours:
                                friendValve = friendNeighbour[1]
                                friendDistance = friendNeighbour[0]
                                if friendRadius - 1 - friendDistance > 1:
                                    friendNew = (friendValve, friendStart, friendRadius - 1 - friendDistance)
                                    argsNew = (humanNew, friendNew)
                                    radiusNew = max(argsNew[0][2], argsNew[1][2])
                                    result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                                    maxPressure = max(maxPressure, friendPressure + result)
                            openedValves.remove(friendStart)
                # HUMAN OPENING
                if humanStart.flowRate > 0 and not openedValves.contains(humanStart):
                    humanPressure = humanStart.flowRate * (humanRadius - 1)
                    openedValves.add(humanStart)
                    for humanNeighbour in humanStart.neighbours:
                        humanValve = humanNeighbour[1]
                        humanDistance = humanNeighbour[0]
                        if humanRadius - 1 - humanDistance > 1:
                            humanNew = (humanValve, humanStart, humanRadius - 1 - humanDistance)
                            # FRIEND NOT OPENING
                            for friendNeighbour in friendStart.neighbours:
                                friendValve = friendNeighbour[1]
                                friendDistance = friendNeighbour[0]
                                if friendRadius - friendDistance > 1 and friendValve != friendPrev:
                                    friendNew = (friendValve, friendStart, friendRadius - friendDistance)
                                    argsNew = (humanNew, friendNew)
                                    radiusNew = max(argsNew[0][2], argsNew[1][2])
                                    result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                                    maxPressure = max(maxPressure, humanPressure + result)
                            # FRIEND OPENING
                            if friendStart.flowRate > 0 and not openedValves.contains(friendStart):
                                friendPressure = friendStart.flowRate * (friendRadius - 1)
                                maxPressure = max(maxPressure, humanPressure + friendPressure)
                                openedValves.add(friendStart)
                                for friendNeighbour in friendStart.neighbours:
                                    friendValve = friendNeighbour[1]
                                    friendDistance = friendNeighbour[0]
                                    if friendRadius - 1 - friendDistance > 1:
                                        friendNew = (friendValve, friendStart, friendRadius - 1 - friendDistance)
                                        argsNew = (humanNew, friendNew)
                                        radiusNew = max(argsNew[0][2], argsNew[1][2])
                                        result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                                        maxPressure = max(maxPressure, friendPressure + humanPressure + result)
                                openedValves.remove(friendStart)
                    openedValves.remove(humanStart)
            # ONLY HUMAN
            else:
                # SOLO FRIEND
                if humanStart.flowRate > 0 and not openedValves.contains(humanStart):
                    humanPressure = humanStart.flowRate * (humanRadius - 1)
                    openedValves.add(humanStart)
                    soloFriendPressure = self.soloMemoryAccess(friendStart, friendPrev, friendRadius, openedValves)
                    maxPressure = max(maxPressure, humanPressure + soloFriendPressure)
                    openedValves.remove(humanStart)
                else:
                    soloFriendPressure = self.soloMemoryAccess(friendStart, friendPrev, friendRadius, openedValves)
                    maxPressure = max(maxPressure, soloFriendPressure)
                # HUMAN NOT OPENING
                for humanNeighbour in humanStart.neighbours:
                    humanValve = humanNeighbour[1]
                    humanDistance = humanNeighbour[0]
                    if humanRadius - humanDistance > 1 and humanValve != humanPrev:
                        humanNew = (humanValve, humanStart, humanRadius - humanDistance)
                        argsNew = (humanNew, friendArgs)
                        radiusNew = max(argsNew[0][2], argsNew[1][2])
                        result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                        maxPressure = max(maxPressure, result)
                # HUMAN OPENING
                if humanStart.flowRate > 0 and not openedValves.contains(humanStart):
                    humanPressure = humanStart.flowRate * (humanRadius - 1)
                    openedValves.add(humanStart)
                    for humanNeighbour in humanStart.neighbours:
                        humanValve = humanNeighbour[1]
                        humanDistance = humanNeighbour[0]
                        if humanRadius - 1 - humanDistance > 1:
                            humanNew = (humanValve, humanStart, humanRadius - 1 - humanDistance)
                            argsNew = (humanNew, friendArgs)
                            radiusNew = max(argsNew[0][2], argsNew[1][2])
                            result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                            maxPressure = max(maxPressure, humanPressure + result)
                    openedValves.remove(humanStart)
        # ONLY FRIEND
        elif radius == friendRadius:
            # SOLO HUMAN
            if friendStart.flowRate > 0 and not openedValves.contains(friendStart):
                friendPressure = friendStart.flowRate * (friendRadius - 1)
                openedValves.add(friendStart)
                soloHumanPressure = self.soloMemoryAccess(humanStart, humanPrev, humanRadius, openedValves)
                maxPressure = max(maxPressure, friendPressure + soloHumanPressure)
                openedValves.remove(friendStart)
            else:
                soloHumanPressure = self.soloMemoryAccess(humanStart, humanPrev, humanRadius, openedValves)
                maxPressure = max(maxPressure, soloHumanPressure)
            # FRIEND NOT OPENING
            for friendNeighbour in friendStart.neighbours:
                friendValve = friendNeighbour[1]
                friendDistance = friendNeighbour[0]
                if friendRadius - friendDistance > 1 and friendValve != friendPrev:
                    friendNew = (friendValve, friendStart, friendRadius - friendDistance)
                    argsNew = (humanArgs, friendNew)
                    radiusNew = max(argsNew[0][2], argsNew[1][2])
                    result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                    maxPressure = max(maxPressure, result)
            # FRIEND OPENING
            if friendStart.flowRate > 0 and not openedValves.contains(friendStart):
                friendPressure = friendStart.flowRate * (friendRadius - 1)
                openedValves.add(friendStart)
                for friendNeighbour in friendStart.neighbours:
                    friendValve = friendNeighbour[1]
                    friendDistance = friendNeighbour[0]
                    if friendRadius - 1 - friendDistance > 1:
                        friendNew = (friendValve, friendStart, friendRadius - 1 - friendDistance)
                        argsNew = (humanArgs, friendNew)
                        radiusNew = max(argsNew[0][2], argsNew[1][2])
                        result = self.friendMemoryAccess(argsNew, radiusNew, openedValves)
                        maxPressure = max(maxPressure, friendPressure + result)
                openedValves.remove(friendStart)
        
        return maxPressure

class Valve:
    def __init__(self, number, label, flowRate, directionList):
        self.number = number
        self.label = label
        self.flowRate = flowRate
        self.directionList = directionList
        self.neighbourList = list()
        self.neighbours = list()
        self.visited = False

    def setDirections(self, valveDict):
        for i in range(len(self.directionList)):
            label = self.directionList[i]
            self.directionList[i] = valveDict.get(label)

    def __lt__(self, other):
        return True

    
def first_part():
    valveList = list()
    valveDict = dict()
    radius = 30
    i = 0
    while True:
        try:
            line = input().split(" ")
        except:
            break
        number = i
        label = line[0]
        flowRate = int(line[1])
        directionList = line[2:]
        valve = Valve(number, label, flowRate, directionList)
        valveDict[label]=valve
        valveList.append(valve)
        if flowRate>0 or label == "AA":
            i += 1
    for v in valveList:
        v.setDirections(valveDict)
    cave = Cave(valveList, valveDict.get("AA"))
    cave.makePaths()
    print(cave.findBestRoute(cave.startingValve, cave.startingValve, radius, OpenedValvesSet()))

def second_part():
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
        flowRate = int(line[1])
        directionList = line[2:]
        valve = Valve(number, label, flowRate, directionList)
        valveDict[label]=valve
        valveList.append(valve)
        if flowRate >0 or label == "AA":
            i += 1
    for v in valveList:
        v.setDirections(valveDict)
    cave = Cave(valveList, valveDict.get("AA"))
    cave.makePaths()
    radius = 26
    humanArgs = (cave.startingValve, cave.startingValve, radius)
    friendArgs = (cave.startingValve, cave.startingValve, radius)
    args = (humanArgs, friendArgs)
    print(cave.findBestRouteWithFriend(args, radius, OpenedValvesSet()))
    
#first_part()
second_part()