import util
from problem import problem
import search
from heuristics import nullHeuristic
from userInput import costGraph, startingPoint, goalPoint, maxFoundInput, heuristicAlla

allaHuristic = lambda state, problem : heuristicAlla(state,problem)
newGraph = util.graphConstruct(costGraph) # Graph {"a":[('c',2)]}

problem = problem(
    graph=newGraph,startPoint=startingPoint,goalPoint=goalPoint,
    is_trace=True, maxFound=maxFoundInput
)

# Solving The Problem
solution=search.breadthfirstsearch(problem)

print(solution)