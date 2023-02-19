
import heapdict
import math


'''
Reading the text file containing info about jugs
First line indicates the capacities of all the different pitchers
Second line indicate target quantity
'''


def readFromFile(textFile):
    with open(textFile, 'r') as f:
        pitchers = [eval(i) for i in f.readline()[:-1].split(",")]
        target = eval(f.readline())

        pitchers = [math.inf] + pitchers
    return target, pitchers


'''
The waterPitcher function that returns the shortest path to get
to target quantity
Return -1 if impossible
'''

'''
def waterPitcher(target, cap):
    # make the first node's value
    # this value has root[0] as the amount in the infinite jug
    root = tuple([0] * len(cap))

    # initialize open and closed list
    openList = [(root, 0, heu(0, root, target))]

    closeList = {}

    loopCounter = -1

    while(openList):
        loopCounter += 1
        # pop the node with the smallest a star values
        # The values in the heapDict are A-star values
        currentState, height, astar = openList.pop()

        print(currentState, height, astar)

        closeList[currentState] = astar
        #closeList.append((currentState, astar))
        currentState = list(currentState)
        print("Close list size:", len(closeList),
              "current state", currentState)

        if(currentState[0] == target):
            return q[1]  # return height

        successors = makeSuccessors(currentState, cap)
        height += 1

        for state in successors:
            astar = height + heu(height, state, target)

            if not inCloseList(state, astar, closeList) and not inOpenList(
                    state, astar, openList) and state[0] <= target:
                openList.append(tuple([height, state, height +
                                      heu(height, state, target)]))

    return -1


def sortFn(elem):
    return elem[2]
'''


def waterPitcher(target, cap):
    # make the first node's value
    # this value has root[0] as the amount in the infinite jug
    root = tuple([0] * len(cap))

    # initialize open and closed list
    openList = heapdict.heapdict()
    openList[(root, 0)] = heu(0, root, target)

    closeList = {}

    while(openList):
        # pop the node with the smallest a star values
        # The values in the heapDict are A-star values
        q, astar = openList.popitem()
        currentState, height = q

        closeList[currentState] = astar
        #closeList.append((currentState, astar))

        if(currentState[0] == target):
            print("Shortest path:", q[1])
            return q[1]  # return height

        successors = makeSuccessors(currentState, cap)
        height += 1

        for state in successors:
            astar = height + heu(height, state, target)

            if not inCloseList(state, astar, closeList) and not inOpenList(
                    state, astar, openList) and state[0] <= target:
                openList[(state, height)] = height +\
                    heu(height, state, target)
    return -1


'''
Function to check whether a state is in closeList
'''


def inCloseList(state, astar, closeList):
    if state in closeList:
        if astar >= closeList[state]:
            return True
    return False


'''
Function to check whether a state is in closeList
'''


def inOpenList(state, astar, openList):
    for elem in openList:
        if (state in elem) and (openList[elem] < astar):
            return True
    return False


'''
Function to generate child nodes
'''


def makeSuccessors(state, cap):
    successors = []
    noOfJugs = len(state)

    for i in range(1, noOfJugs):
        jugs = list(state)

        # Fill jugs
        if(jugs[i] == 0):
            jugs[i] = cap[i]
            successors.append(tuple(jugs))

        else:
            for j in range(noOfJugs):
                jugs = list(state)

                # pour between jugs
                if (jugs[j] < cap[j]) and (i != j):
                    transfer = min(jugs[i], cap[j] - jugs[j])
                    jugs[i] -= transfer
                    jugs[j] += transfer

                # empty to ground
                else:
                    jugs[i] = 0

                successors.append(tuple(jugs))

    return successors


'''
A-star function calculates the A-star score f
'''
'''

def heu(cost, currentState, target):
    temp = []
    total = target - currentState[0]
    jugs = currentState[1:]
    for state in jugs:
        temp.append(abs(state - total) + cost)
    return (min(temp)) / target


'''


def heu(cost, state, target):
    h = 0
    d = abs(target - state[0])
    if(d == 0):
        return 0
    for i in state:
        h += abs(d - i)
        h /= (d)
    return h


'''
def waterPitcher(target, cap):
    # make the first node's value
    # this value has root[0] as the amount in the infinite jug
    root = tuple([0] * len(cap))

    # initialize open and closed list
    openList = heapdict.heapdict()
    openList[(root, 0)] = heu(0, root, target)

    closeList = {}

    while(openList):
        # pop the node with the smallest a star values
        # The values in the heapDict are A-star values
        q, astar = openList.popitem()
        currentState, height = q
        print(currentState, height, astar)
        closeList[currentState] = astar
        #closeList.append((currentState, astar))

        print("Close list size:", len(closeList))
        if(currentState[0] == target):
            return q[1]  # return height

        successors = makeSuccessors(currentState, cap)
        height += 1

        for state in successors:
            astar = height + heu(height, state, target)

            if not inCloseList(state, astar, closeList) and not inOpenList(
                    state, astar, openList) and state[0] <= target:
                openList[(state, height)] = height +\
                    heu(height, state, target)

    return -1
'''

'''
input: 1,4,10,15,22 = 181 (19)
input1: 2,5,6,73 = 143 (7)
input2: 3,6 = 2 (impossible)
input3: 2 = 143 (impossible)
input4: 2,3,5,19,121,852 = 11443 (36)
'''


def main():
    target, cap = readFromFile("input5.txt")
    #prompt = [1, [1, 3]]
    print("Shortest path is:", waterPitcher(target, cap))
    # test()


if __name__ == '__main__':
    main()
