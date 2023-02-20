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


def waterPitcher(target, cap):
    # make the first node's value
    # this value has root[0] as the amount in the infinite jug
    root = tuple([0] * len(cap))

    # initialize open and closed list
    openList = heapdict.heapdict()
    openList[(root, 0, ())] = heu(root, target)

    closeList = {}

    while openList:
        # pop the node with the smallest a star values
        # The values in the heapDict are A-star values
        key, astar = openList.popitem()

        # keys in the heapDict contains 3 values: state, height, and path
        currentState, height, path = key

        # Change path back to list in order to append
        path = list(path)
        path.append(currentState)

        closeList[currentState] = astar

        if(currentState[0] == target):
            return key[1], path  # return height

        successors = makeSuccessors(currentState, cap)

        for state in successors:
            if state not in closeList and state[0] <= target:
                openList[(state, height + 1, tuple(path))
                         ] = heu(state, target) + height + 1

    return -1, []


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


def heu(state, target):
    d = target - state[0]

    temp = []

    jugs = state[1:]
    for i in jugs:
        temp.append(abs(i - d))

    return (min(temp) / len(state))


'''
input: 1,4,10,15,22 = 181 (19)
input1: 2,5,6,73 = 143 (7)
input2: 3,6 = 2 (impossible)
input3: 2 = 143 (impossible)
input4: 2,3,5,19,121,852 = 11443 (36)
'''


def main():
    target, cap = readFromFile("input\input5.txt")
    cost, path = waterPitcher(target, cap)
    # prompt = [1, [1, 3]
    print("Shortest path is:", path, "\nCost:", cost)
    print(len(path) - 1)
    # test()


if __name__ == '__main__':
    main()
