import numpy

class Knot:
    def __init__(self):
        self.position = [0,0]
        self.visitedPoints = {(0,0)}

    def follow(self, head):
        displacement = [head.position[0]-self.position[0], head.position[1]-self.position[1]]
        while abs(displacement[0])>1 or abs(displacement[1])>1 :
            if abs(displacement[0]) > 0:
                if abs(displacement[1]) > 0:
                    self.position[1] += numpy.sign(displacement[1])
                self.position[0] += numpy.sign(displacement[0])
            else:
                self.position[1] += numpy.sign(displacement[1])
            displacement = [head.position[0]-self.position[0], head.position[1]-self.position[1]]
            self.visitedPoints.add((self.position[0], self.position[1]))

class Rope:
    def __init__(self, size):
        self.size = size
        self.knots = []
        for i in range (0, size):
            self.knots.append(Knot())

    def move_head(self, direction, distance):
        if direction == "R":
            while distance > 0:
                self.knots[0].position[0] += 1
                distance -= 1
                for i in range (1, self.size):
                    self.knots[i].follow(self.knots[i-1])
        elif direction == "L":
            while distance > 0:
                self.knots[0].position[0] -= 1
                distance -= 1
                for i in range (1, self.size):
                    self.knots[i].follow(self.knots[i-1])
        elif direction == "U":
            while distance > 0:
                self.knots[0].position[1] += 1
                distance -= 1
                for i in range (1, self.size):
                    self.knots[i].follow(self.knots[i-1])
        elif direction == "D":
            while distance > 0:
                self.knots[0].position[1] -= 1
                distance -= 1
                for i in range (1, self.size):
                    self.knots[i].follow(self.knots[i-1])

    def visitedPoints(self):
        return len(self.knots[self.size-1].visitedPoints)

def first_part():
    rope = Rope(2)
    while True:
        try: line = input()
        except: break
        splitLine = line.split(" ")
        direction = splitLine[0]
        distance = int(splitLine[1])
        rope.move_head(direction, distance)
    print(rope.visitedPoints())

def second_part():
    rope = Rope(10)
    while True:
        try: line = input()
        except: break
        splitLine = line.split(" ")
        direction = splitLine[0]
        distance = int(splitLine[1])
        rope.move_head(direction, distance)
    print(rope.visitedPoints())

second_part()

        

