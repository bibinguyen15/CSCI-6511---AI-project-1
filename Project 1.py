from collections import deque
import re
from Classes import TreeNode

'''
Reading the text file containing info about jugs
First line indicates the capacities of all the different pitchers
Second line indicate target quantity
'''
def readFromFile(textFile):
    with open(textFile, 'r') as f:
        pitchers = [eval(i) for i in f.readline()[:-1].split(" ")]
        target = eval(f.readline())
 
    return [target, pitchers]


'''
The waterPitcher function that returns the shortest path to get
to target quantity
Return -1 if impossible
'''
def waterPitcher(prompt):
    #get target and pitchers
    target = prompt[0]
    pitchers = prompt[1]
    numPitch = len(pitchers)
    print("Number of Pitchers:", numPitch)
    print("Pitcher sizes:", pitchers, "\nTarget: ", target, "\n")
    
    #make the first node
    root = [0]*(len(pitchers) + 1)
    
    
    #initialize open and closed list
    openList = [root]
    closeList = []
    
    #Add first node to tree

    firstNode = TreeNode(root, 0, heu(root))
    
    
    while(openList):
        print(openList)
        q = openList[0]
        
        openList.pop(0)
        print(openList)
    
'''
A-star function calculates the A-star score f
'''
def heu(state):
    return 1

def srtFn(item):
    return item[0]

def compareAndReplace(list, state):
    for sub in list:
        if(sub[1] == state):
            return list.index(sub)

def test():
    openList = [
        [10, [0, 4, 2, 5]],
        [5, [0, 1, 2, 3]],
        [7, [10, 2,4,2]],
        [2, [0, 1, 2, 3]]]
    print(openList)
    openList.sort(key= srtFn)
    
    state1 = [0, 1, 2, 3]
    
    index = compareAndReplace(openList, state1)
    openList.pop(index)
    print(openList)
    
    listOfZeroes = [0] * 10
    print(listOfZeroes)
    

    
def main():
    prompt = readFromFile("test1.txt")
    waterPitcher(prompt)
    test()
    

if __name__ == '__main__':
    main()
    