import util
from heuristics import nullHeuristic

def breadthfirstsearch(problem):
    explored = set()
    fringe = util.Queue()
    fringe.push(
        (problem.getStartState(), [problem.getStartState()], 0)
    )
    while not fringe.isEmpty():
        curState, curDirections, curCost = fringe.pop()
        explored.add("->".join(map(str, curDirections)))
        if problem.isGoalState(curState):
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

def depthfirstsearch(problem):
    return []

def uniformCostSearch(problem):
    return []

def greedySearch(problem,heuristic=nullHeuristic):
    return []
def aStarSearch(problem, heuristic=nullHeuristic):
      
    return []

#########################

def printChosenState(problem, curDirections,curState):
    problem.printDirection(curDirections)
    print("| ",end="")
    if problem.isGoalState(curState,addCount=False):  print(" { Goal Achieved }")
    
def printFringe(problem,fringe):
    problem.printPriorityQueue(fringe)
    print()