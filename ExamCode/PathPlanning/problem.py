import util
class problem:
    def __init__(self,graph, startPoint, goalPoint, is_trace,maxFound):
        self.graph = graph
        self.startPoint = startPoint
        self.goalPoint = goalPoint
        self.is_trace = is_trace
        self.maxFound = maxFound
        self.count=0

    def isTrace(self):
        return self.is_trace
    def isGoalState(self, curState, addCount=True):
        if self.goalPoint == curState and addCount:
            self.count=self.count+1
        return self.goalPoint == curState
    
    def shouldEnd(self):
        return self.count == self.maxFound
    
    def getStartState(self):
        return self.startPoint
    
    def getSuccessors(self,curState):
        return self.graph[curState]
    
    def getCost(self,curState, futureState):
        if curState == futureState:
            return 0
        Costs= self.graph[curState]
        for tup in Costs:
            if tup[0] == futureState:
                return tup[1]
    
    def printDirection(self,solution,priority=-1):
        ac_cost=0
        prevNode= self.startPoint
        for node in solution:
            ac_cost+=self.getCost(prevNode,node)
            prevNode = node 
        
        if priority!=-1:
            ac_cost = priority
        result = "".join(map(str, solution))
        print(f"({result},{ac_cost})",end="")

    def printPriorityQueue(self, fringe):
        endx=""
        for priority,count,tup in fringe.heap:
            print(endx,end="")
            endx=","
            self.printDirection(tup[1],priority=priority)