import numpy

class Polyline:
    def __init__(self, line):
        splitLine = line.split(" -> ")
        self.points = list()
        for s in splitLine:
            temp = tuple(s.split(','))
            self.points.append((int(temp[0]), int(temp[1])))
    def minX(self):
        min = self.points[0][0]
        for p in self.points:
            if p[0] < min:
                min = p[0]
        return min
    def minY(self):
        min = self.points[0][1]
        for p in self.points:
            if p[0] < min:
                min = p[1]
        return min
    def maxX(self):
        max = self.points[0][0]
        for p in self.points:
            if p[0] > max:
                max = p[0]
        return max
    def maxY(self):
        max = self.points[0][1]
        for p in self.points:
            if p[0] > max:
                max = p[1]
        return max
    def simplify(self, minX, minY):
        for i in range(0, len(self.points)):
            self.points[i] = (self.points[i][0]-minX, self.points[i][1]-minY)

    def fillCave(self, cave):
        for i in range (len(self.points)-1):
            x = self.points[i][0]
            y = self.points[i][1]
            xLimit = self.points[i+1][0]
            yLimit = self.points[i+1][1]
            cave.places[y][x] = 1
            while x != xLimit or y != yLimit:
                x += numpy.sign(xLimit - x)
                y += numpy.sign(yLimit - y)
                cave.places[y][x] = 1


class Cave:
    def __init__(self, width, height, sandOrigin):
        self.width = width + 3
        self.height = height + 3
        self.sandX = sandOrigin[0]
        self.sandY = sandOrigin[1]
        self.places = [[] for i in range (self.height)]
        for i in range (self.height):
            for j in range (self.width):
                self.places[i].append(0)
        self.places[self.sandY][self.sandX] = 2

    def voidFill(self, polylineList):
        for i in range (self.width):
            self.places[self.height-2][i] = 4
        for p in polylineList:
            p.fillCave(self)

    def rockFill(self, polylineList):
        for i in range (self.width):
             self.places[self.height-1][i] = 1
        for p in polylineList:
            p.fillCave(self)


    def fillWithSand(self):
        amountOfSand = 0
        while self.dropSand():
            amountOfSand += 1
        return amountOfSand
    
    def dropSand(self):
        order = []
        order.append([self.sandX, self.sandY+1])
        order.append([self.sandX-1, self.sandY+1])
        order.append([self.sandX+1, self.sandY+1])
        i = 0
        while True:
            i+= 1
            for o in order:
                if self.places[o[1]][o[0]] == 4:
                    return False
                elif self.places[o[1]][o[0]] == 0:
                    order[0] = [o[0], o[1]+1]
                    order[1] = [order[0][0]-1, order[0][1]]
                    order[2] = [order[0][0]+1, order[0][1]]
                    break
            if self.places[order[0][1]][order[0][0]] == 1 and self.places[order[1][1]][order[1][0]] == 1 and self.places[order[2][1]][order[2][0]] == 1: break
            if i == 1000: break
        x = order[0][0]
        y = order[0][1] - 1
        if x == self.sandX and y == self.sandY and self.places[y][x] == 1: return False
        self.places[y][x] = 1
        return True

    def printCave(self):
        for pList in self.places:
            for p in pList:
                print(p, end="")
            print()


        
        
def first_part():
    polylineList = list()
    minX = 500
    minY = 0
    maxX = 500
    maxY = 0
    while True:
        try:
            poly = Polyline(input())
            polylineList.append(poly)
        except:
            break
    for p in polylineList:
        p_minX = p.minX()
        p_minY = p.minY()
        p_maxX = p.maxX()
        p_maxY = p.maxY()
        if(p_minX < minX): minX = p_minX
        if(p_minY < minY): minY = p_minY
        if(p_maxX > maxX): maxX = p_maxX
        if(p_maxY > maxY): maxY = p_maxY
    minX -= 1
    maxX -= 1
    width = maxX - minX
    height = maxY - minY
    sandOrigin = (500-minX, 0-minY)
    for p in polylineList:
        p.simplify(minX, minY)
    cave = Cave(width, height, sandOrigin)
    cave.voidFill(polylineList)
    print(cave.fillWithSand())

def second_part():
    polylineList = list()
    minX = 500
    minY = 0
    maxX = 500
    maxY = 0
    while True:
        try:
            poly = Polyline(input())
            polylineList.append(poly)
        except:
            break
    for p in polylineList:
        p_minX = p.minX()
        p_minY = p.minY()
        p_maxX = p.maxX()
        p_maxY = p.maxY()
        if(p_minX < minX): minX = p_minX
        if(p_minY < minY): minY = p_minY
        if(p_maxX > maxX): maxX = p_maxX
        if(p_maxY > maxY): maxY = p_maxY
    if(500 - minX < maxX - 500) :
        minX = 1000 - maxX
    elif(500 - minX > maxX - 500):
        maxX = 1000 - minX
    width = maxX - minX
    height = maxY - minY
    if 2*height > width:
        minX -= 2*height - width
        maxX += 2*height - width
        width = maxX - minX
    sandOrigin = (500-minX, 0-minY)
    for p in polylineList:
        p.simplify(minX, minY)
    cave = Cave(width, height, sandOrigin)
    cave.rockFill(polylineList)
    print(cave.fillWithSand())
    
#first_part()
second_part()