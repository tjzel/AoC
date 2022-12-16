class Sensor:
    def __init__(self, points):
        self.myX = int(points[0])
        self.myY = int(points[1])
        self.beaconX = int(points[2])
        self.beaconY = int(points[3])

class Section:
    def __init__(self, sensor, row):
        if sensor != None:
            self.row = row
            sensorX = sensor.myX
            sensorY = sensor.myY
            beaconX = sensor.beaconX
            beaconY = sensor.beaconY
            radius = abs(sensorX - beaconX) + abs(sensorY - beaconY)
            reducedRadius = radius - abs(sensorY - self.row)
            if reducedRadius < 0:
                self.left = None
                self.right = None
                self.length = 0
            else:
                self.left = sensorX - reducedRadius
                self.right = sensorX + reducedRadius
                self.length = self.right - self.left + 1

    def limit(self, lower, upper):
        if lower != None and self.length > 0:
            self.left = max(self.left, lower)
            self.left = min(self.left, upper)
            self.right = min(self.right, upper)
            self.right = max(self.right, lower)
            self.length = self.right - self.left + 1

    def __lt__(self, other):
        return self.left < other.left

    def splitIntersection(self, b, lower, upper):
        left = 0
        right = -1
        length = 0
        if self.left <= b.left and self.right >= b.left:
            b.left = self.right + 1
        elif b.left < self.left and b.right >= self.left:
            if b.right >= self.right:
                right = b.right
                left = self.right + 1
            b.right = self.left - 1
        b.length = b.right - b.left + 1
        length = right - left + 1
        self.limit(lower, upper)
        if length > 0:
            section = Section(None, None)
            section.left = left
            section.right = right
            section.length = length
            section.row = self.row
            section.limit(lower, upper)
            return section
        else:
            return None

def countBlockedInRow(sensorList, beaconSet, row, lower, upper):
    sectionList = list()
    for sensor in sensorList:
        section = Section(sensor, row)
        section.limit(lower, upper)
        if section.length != 0:
            for S in sectionList:
                tempList = list()
                leftover = S.splitIntersection(section, lower, upper)
                if leftover != None:
                    tempList.append(leftover)
                while len(tempList) > 0 :
                    temp = tempList.pop()
                    for subS in sectionList:
                        leftover = subS.splitIntersection(temp, lower, upper)
                        if temp.length < 0:
                            break
                        if leftover != None:
                            tempList.append(leftover)
                    if temp.length > 0:
                        sectionList.append(temp)
            if section.length > 0:
                sectionList.append(section)
    sectionList.sort()
    sum = 0
    x = None
    if sectionList[0].left != lower:
        x = lower
    elif sectionList[len(sectionList)-1].right != upper:
        x = upper
    
    for i in range(len(sectionList)):
        sum += sectionList[i].length
        temp = sectionList[i].right + 1
        if i<len(sectionList)-1:
            if temp != sectionList[i+1].left:
                x = temp
    for b in beaconSet:
        if b[1] == row:
            for s in sectionList:
                if b[0]>=s.left and b[0]>=s.right:
                    sum -= 1
                    break
    return (sum, x)


def first_part():
    row = 2000000
    #row = 10
    sensorList = list()
    beaconSet = set()
    while True:
        try:
            line = input().split(" ")
        except:
            break
        beaconSet.add((int(line[2]), int(line[3])))
        sensor = Sensor(line)
        sensorList.append(sensor)
    sum = countBlockedInRow(sensorList, beaconSet, row, None, None)
    print(sum[0])

def second_part():
    sensorList = list()
    beaconSet = set()
    lower = 0
    upper = 4000000
    # lower = 0
    # upper = 20
    while True:
        try:
            line = input().split(" ")
        except:
            break
        beaconSet.add((int(line[2]), int(line[3])))
        sensor = Sensor(line)
        sensorList.append(sensor)
    for i in range(lower, upper+1):
        pair = countBlockedInRow(sensorList, list(), i, lower, upper)
        if pair[1] != None:
            print(pair[1]*upper + i)
            return

    

#first_part()
second_part()
        

        
