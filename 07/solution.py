import re

class Node:
    cutoff = 100000
    totalSpace = 70000000
    requiredFree = 30000000
    currentFree = 0
    def __init__(self, name, parent, children, size):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

    def addUp(self, fileSize):
        self.size += fileSize
        if self.parent != None:
            self.parent.addUp(fileSize)

    def sumDown(self):
        sum = 0
        for c in self.children:
            sum += c.sumDown()
        if self.size <= self.cutoff:
            sum += self.size
        return sum
    
    def findFitting(self, currentMin):
        if self.size < currentMin and Node.currentFree + self.size >= Node.requiredFree:
            currentMin = self.size
        for c in self.children:
            currentMin = c.findFitting(currentMin)
        return currentMin

    

class Tree:
    def __init__(self, root):
        self.root = root

def first_part(fileTree):
    print(fileTree.root.sumDown())

def second_part(fileTree):
    Node.currentFree = Node.totalSpace - rootDir.size
    print(fileTree.root.findFitting(fileTree.root.size))

rootDir = Node("/",None,[],0)
fileTree = Tree(rootDir)
currentDir = rootDir

while True:
    try:
        line = input()
    except:
        break
    if re.match("^\$ cd", line):
        dirName = re.sub("^\$ cd ", "", line)
        if dirName == "/":
            currentDir = fileTree.root
        elif dirName == "..":
            currentDir = currentDir.parent
        else:
            for c in currentDir.children:
                if c.name == dirName:
                    currentDir = c
                    break
    elif re.match("^dir ", line):
        dirName = re.sub("^dir ", "", line)
        currentDir.children.append(Node(dirName, currentDir, [], 0))
    elif re.match("^[0-9]+", line):
        fileSize = int(re.match("^[0-9]+", line)[0])
        fileName = re.sub("^[0-9]+ ", "", line)
        currentDir.addUp(fileSize)

first_part(fileTree)
second_part(fileTree)