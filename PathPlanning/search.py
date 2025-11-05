import util
from heuristics import nullHeuristic

def breadthfirstsearch(problem):
    cc=0
    explored = set()
    fringe = util.Queue()
    fringe.push(
        (problem.getStartState(), [problem.getStartState()], 0)
    )
    while not fringe.isEmpty():
        curState, curDirections, curCost = fringe.pop()
        explored.add("->".join(map(str, curDirections)))
        if problem.isGoalState(curState):
            cc+=1
            print(cc,end="-  ")
            printChosenState(problem, curDirections, curState)
            if problem.shouldEnd():
                return curDirections
            continue
        for state, cost in problem.getSuccessors(curState):
            if not ("->".join(map(str, curDirections + [state])) in explored) and not problem.isGoalState(
                    curDirections[-1],False) and not (state in curDirections):
                new_priority = curCost + cost
                fringe.push((state, curDirections + [state], curCost + cost))
    print("Failure"); return []

def depthfirstsearch(problem):
    explored = set()
    fringe = util.Stack()
    fringe.push(
        (problem.getStartState(), [problem.getStartState()], 0)
    )
    while not fringe.isEmpty():
        curState, curDirections, curCost = fringe.pop()
        explored.add("->".join(map(str, curDirections)))
        if problem.isGoalState(curState):
            printChosenState(problem, curDirections, curState)
            if problem.shouldEnd():
                return curDirections
            else:
                continue
        for state, cost in problem.getSuccessors(curState):
            if not ("->".join(map(str, curDirections + [state])) in explored) and not problem.isGoalState(
                    curDirections[-1]) and not (state in curDirections):
                new_priority = curCost + cost
                fringe.push((state, curDirections + [state], curCost + cost))
    print("Failure")
    return []

def uniformCostSearch(problem):
    return aStarSearch(problem)

def greedySearch(problem,heuristic=nullHeuristic):
    costFunc= lambda x: 0
    return aStarSearch(problem, heuristic,costFunc)
def aStarSearch(problem, heuristic=nullHeuristic, costFunc=lambda x: x):
    explored = set()
    fringe = util.PriorityQueue()
    fringe.push(
        (problem.getStartState(), [problem.getStartState()], 0),
        heuristic(problem.getStartState(), problem)
    )
    while not fringe.isEmpty():
        curState, curDirections, curCost = fringe.pop()
        explored.add("->".join(map(str,curDirections) ) )
        if problem.isTrace(): printChosenState(problem, curDirections,curState)
        if problem.isGoalState(curState):
            if problem.shouldEnd(): 
                return curDirections
            else:
                continue
        for state, cost in problem.getSuccessors(curState):
            if not ("->".join(map(str,curDirections+[state]) ) in explored) and not problem.isGoalState(curDirections[-1]) and not (state in curDirections):
                new_priority = costFunc(curCost + cost) + heuristic(state, problem)
                fringe.push((state, curDirections + [state], curCost + cost), new_priority)
        if problem.isTrace(): printFringe(problem,fringe)
    print("Failure")        
    return []
#########################
def printChosenState(problem, curDirections,curState):
    problem.printDirection(curDirections)
    print("| ",end="")
    if problem.isGoalState(curState,addCount=False):  print(" { Goal Achieved }")
    
def printFringe(problem,fringe):
    problem.printPriorityQueue(fringe)
    print()