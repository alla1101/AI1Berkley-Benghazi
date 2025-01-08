import util
from heuristics import nullHeuristic

def breadthfirstsearch(problem):
   
    return []

def depthfirstsearch(problem):
    
    return []

def uniformCostSearch(problem):
    return aStarSearch(problem)

def greedySearch(problem,heuristic=nullHeuristic):
    costFunc= lambda x: 0
    return aStarSearch(problem, heuristic,costFunc)

def aStarSearch(problem, heuristic=nullHeuristic, costFunc=lambda x: x):
      
    return []

#########################

def printChosenState(problem, curDirections,curState):
    problem.printDirection(curDirections)
    print("| ",end="")
    if problem.isGoalState(curState,addCount=False):  print(" { Goal Achieved }")
    
def printFringe(problem,fringe):
    problem.printPriorityQueue(fringe)
    print()