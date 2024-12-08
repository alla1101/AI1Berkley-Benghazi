import util
def BreadthFirstSearch(problem):

    explored = set()
    fringe = util.Queue()
    fringe.push( (problem.getStartState(), [problem.getStartState()] ) )

    while not fringe.isEmpty():
        curState, curDirections = fringe.pop()
        explored.add("->".join(map(str,curDirections) ) )
        # Trace        
        printChosenState(problem, curDirections,curState)

        if problem.isGoalState(curDirections):
            return curDirections
            
        for state in problem.getSuccessors(curState):

            if not ("->".join(map(str,curDirections+[state]) ) in explored) and not problem.isGoalState(curDirections) and not (state in curDirections):
                fringe.push((state, curDirections + [state] ) )

    print("Failure")        
    return []

def printChosenState(problem, curDirections,curState):
    problem.printDirection(curDirections)
    print()
    if problem.isGoalState(curDirections):  print(" { Goal Achieved }")
    
