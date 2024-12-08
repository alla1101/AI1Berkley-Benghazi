import util
class problem:
    def __init__(self,graph, startPoint):
        self.graph = graph
        self.startPoint = startPoint
        self.count=0
    def isGoalState(self, curDirections):
        if len(curDirections) < 8:
            return False
        prev = -1
        for node in curDirections:
            if prev > node:
                return False
            prev = node
        return True
    def getStartState(self):
        return self.startPoint
    def getSuccessors(self,state):
        return self.graph     
    def printDirection(self,solution):
        result = "".join(map(str, solution))
        print(f"({result})",end="")