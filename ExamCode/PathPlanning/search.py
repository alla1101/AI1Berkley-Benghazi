import util
from heuristics import nullHeuristic

def breadthfirstsearch(problem):
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