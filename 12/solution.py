import queue

class Square:
    def __init__(self, key, position):
        self.key = ord(key) - ord('a')
        self.position = position
        self.directions = []
        self.visited = 0
    def update(self, neighbourPosition, neighbour):
        if abs(self.key - neighbour.key) <= 1:
            self.directions.append(neighbourPosition)
    def __lt__(self, other): return True

class Map:
    def __init__(self):
        return
    def loadMap(self):
        line = input()
        self.length = 0
        self.width = len(line)
        self.squares = []
        while True:
            self.squares.append([])
            for i in range(0, self.width):
                if line[i] == 'S':
                    self.start = (i, self.length)
                    self.squares[self.length].append(Square('a', (self.length, i)))
                elif line[i] == 'E':
                    self.end = (i, self.length)
                    self.squares[self.length].append(Square('z', (self.length, i)))
                else: self.squares[self.length].append(Square(line[i], (self.length, i)))
            self.length += 1
            try: line = input()
            except: break
        for i in range (0, self.length):
            for j in range(0, self.width):
                if j>0: 
                    self.squares[i][j].update((i,j-1), self.squares[i][j-1])
                if j<self.width-1: 
                    self.squares[i][j].update((i,j+1), self.squares[i][j+1])
                if i<0: 
                    self.squares[i][j].update((i-1,j), self.squares[i-1][j])
                if i<self.length-1: 
                    self.squares[i][j].update((i+1,j), self.squares[i+1][j])
    def findShortest(self):
        objectQueue = queue.PriorityQueue()
        length = self.start[0]
        width = self.start[1]
        self.squares[length][width].visited = 1
        objectQueue.put((0, self.squares[length][width]))
        while True:
            currentObject = objectQueue.get()
            currentPos = currentObject[1].position
            if currentPos == self.end:
                return currentObject[0]
            length = currentObject[1].position[0]
            width = currentObject[1].position[1]
            print(length, width)
            for d in currentObject[1].directions:
                length = d[0]
                width = d[1]
                distance = currentObject[0] + 1
                if self.squares[length][width].visited == 0:
                    self.squares[length][width].visited = 1
                    objectQueue.put((distance, self.squares[length][width]))

    def print(self):
        for sq in self.squares:
            for s in sq:
                #print(chr(s.key+ord('a')), end=" ")
                print(len(s.directions), end=" ")
            print()

        
map = Map()
map.loadMap()
map.print()
print(map.findShortest())