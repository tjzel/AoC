import re

class Node:
    def __init__(self, name, parent, children, size):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

    def addUp(self, fileSize):
        self.size += fileSize
        if self.parent != None:
            self.parent.addUp(fileSize)

class Tree:
    def __init__(self, root):
        self.root = root

sum = 0

rootDir = Node("/",None,[],0)
fileTree = Tree(rootDir)
currentDir = rootDir

while True:
    try:
        line = input()
    except:
        break
    if re.match("^\$ cd", line):
        #print(line)
        dirName = re.sub("^\$ cd ", "", line)
        print("!!!", dirName)
        print("available children:")
        for c in currentDir.children:
            print("\t", c.name)
        #print(dir)
        #print()
        if dirName == "/":
            currentDir = fileTree.root
        elif dirName == "..":
            currentDir = currentDir.parent
        else:
            for c in currentDir.children:
                if c.name == dirName:
                    currentDir = c
                    break
        print("entered:", currentDir.name)
        print()
    elif re.match("^dir ", line):
        dirName = re.sub("^dir ", "", line)
        print("adding " + dirName)
        currentDir.children.append(Node(dirName, currentDir, [], 0))
    elif re.match("^[0-9]+", line):
        fileSize = int(re.match("^[0-9]+", line)[0])
        fileName = re.sub("^[0-9]+ ", "", line)
        #print("file size:", fileSize, "file name:", fileName)
        currentDir.addUp(fileSize)
        #print(currentDir.size)
    