from functools import cmp_to_key
import copy

class Packet:
    def __init__(self, data):
        self.data = data.split(' ')
        self.dataLimit = len(self.data)
    def compare(up, do):
        up = copy.deepcopy(up)
        do = copy.deepcopy(do)
        result = 0
        u = 0
        uLimit = up.dataLimit
        d = 0
        dLimit = do.dataLimit
        while result == 0:
            if u == uLimit: result = -1
            elif d == dLimit: result = 1
            else:
                if up.data[u] == '[':
                    if do.data[d] == ']':
                        result = 1
                    elif do.data[d] != '[':
                        do.data.insert(d+1, ']')
                        do.data.insert(d, '[')
                        dLimit += 2
                elif up.data[u] == ']':
                    if do.data[d] != ']':
                        result = -1
                else:
                    if do.data[d] == '[':
                        up.data.insert(u+1, ']')
                        up.data.insert(u, '[')
                        uLimit += 2
                    elif do.data[d] == ']':
                        result = 1
                    elif int(up.data[u]) < int(do.data[d]):
                        result = -1
                    elif int(up.data[u]) > int(do.data[d]):
                        result = 1
                u+=1
                d+=1
        return result

def first_part():
    i = 1
    sum = 0
    while True:
        up = Packet(input())
        do = Packet(input())
        result = Packet.compare(up, do)
        if(result == -1): 
            sum += i
        i+=1
        try:
            input()
        except:
            break
    print(sum)

def second_part():
    packetList = []
    while True:
        up = Packet(input())
        packetList.append(up)
        do = Packet(input())
        packetList.append(do)
        try:
            input()
        except:
            break
    packetList.append(Packet("[ 2 ]"))
    packetList.append(Packet("[ 6 ]"))
    sortedList = sorted(packetList, key=cmp_to_key(Packet.compare))
    start = 0
    end = 0
    for i in range(0, len(sortedList)):
        if sortedList[i].data == ['[', '2', ']']: 
            start = i+1
        elif sortedList[i].data ==['[', '6', ']']:
            end = i+1
    print(start*end)


   
#first_part()
second_part()
                

            
