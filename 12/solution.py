import queue

class Square:
    def __init__(self, key, position):
        self.key = ord(key) - ord('a')
        self.position = position
        self.directions = []
        self.visited = 0
    def update(self, neighbour):
        if self.key - neighbour.key > -2:
            self.directions.append(neighbour.position)
    def visit(self):
        self.visited = 1
    def unvisit(self):
        self.visited = 0
    def __lt__(self, other): return True

class Map:
    def __init__(self):
        return
    def loadMap(self):
        line = input()
        self.length = 0
        self.width = len(line)
        self.squares = []
        self.startPoints = []
        while True:
            self.squares.append([])
            for i in range(0, self.width):
                if line[i] == 'S':
                    self.start = (self.length, i)
                    self.squares[self.length].append(Square('a', (self.length, i)))
                elif line[i] == 'E':
                    self.end = (self.length, i)
                    self.squares[self.length].append(Square('z', (self.length, i)))
                elif line[i] == 'a':
                    self.squares[self.length].append(Square('a', (self.length, i)))
                    self.startPoints.append((self.length, i))
                else: self.squares[self.length].append(Square(line[i], (self.length, i)))
            self.length += 1
            try: line = input()
            except: break
        for i in range (0, self.length):
            for j in range(0, self.width):
                if j>0: 
                    self.squares[i][j].update(self.squares[i][j-1])
                if j<self.width-1: 
                    self.squares[i][j].update(self.squares[i][j+1])
                if i>0: 
                    self.squares[i][j].update(self.squares[i-1][j])
                if i<self.length-1: 
                    self.squares[i][j].update(self.squares[i+1][j])
    def findShortest(self, start):
        self.unvisitAll()
        objectQueue = queue.PriorityQueue()
        length = start[0]
        width = start[1]
        self.squares[length][width].visit()
        objectQueue.put((0, self.squares[length][width]))
        while True:
            if(objectQueue.empty()): return 0
            currentObject = objectQueue.get()
            currentPos = currentObject[1].position
            if currentPos == self.end:
                return currentObject[0]
            length = currentObject[1].position[0]
            width = currentObject[1].position[1]
            for d in currentObject[1].directions:
                length = d[0]
                width = d[1]
                distance = currentObject[0] + 1
                if self.squares[length][width].visited == 0:
                    self.squares[length][width].visit()
                    objectQueue.put((distance, self.squares[length][width]))
            if(objectQueue.empty()):
                return -1
    
    def unvisitAll(self):
        for sRow in self.squares:
            for s in sRow:
                s.unvisit()

def first_part():
    map = Map()
    map.loadMap()
    print(map.findShortest(map.start))

def second_part():
    map = Map()
    map.loadMap()
    min = map.findShortest(map.start)
    for m in map.startPoints:
        temp = map.findShortest(m)
        if temp != -1 and temp < min: min = temp
    print(min)

#first_part()
second_part()