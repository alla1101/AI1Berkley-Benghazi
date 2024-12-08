from problem import problem
import search

def heuristicAlla(state,problem):
    matrixA= [
        ["r","r","r","r","r","r","r"],
        ["r",0,"r",4,4,3,"r"],
        ["r",1,3,2,1,5,"r"],
        ["r",0,"r",6,8,0,"r"],
        ["r",2,16,3,2,19,"r"],
        ["r",4,7,4,"r",1,"r"],
        ["r",4,3,5,1,0,"r"],
        ["r","r","r","r","r","r","r"]
    ]
    cost=matrixA[int(state[2])][int(state[1])]
    if cost == 'r':
        return 0
    return cost
newGraph={
    "x11": [("x21",1)],"x12": [("x22",3),("x11",0),("x13",4)],"x13": [("x23",2),("x14",4)],"x14": [("x24",1),("x13",4),("x15",3)],"x15": [("x25",5),("x14",4)],
    "x21": [("x11",0),("x31",0),("x22",3)],"x22": [("x21",1),("x23",2)],"x23": [("x13",4),("x33",6),("x22",3),("x24",1)],"x24": [("x14",4),("x34",8),("x23",2),("x25",5)],"x25": [("x15",3),("x35",0),("x24",1)],
    "x31": [("x21",1),("x41",2)],"x32": [("x22",3),("x42",16),("x31",0),("x33",6)],"x33": [("x23",2),("x43",3),("x34",8)],"x34": [("x24",1),("x44",2),("x33",6),("x35",0)],"x35": [("x25",5),("x45",19),("x34",8)],
    "x41": [("x31",0),("x51",4),("x42",16)],"x42": [("x52",7),("x41",2),("x43",3)],"x43": [("x33",6),("x53",4),("x42",16),("x44",2)],"x44": [("x34",8),("x43",3),("x45",19)],"x45": [("x35",0),("x55",1),("x44",2)],
    "x51": [("x41",2),("x61",4),("x52",7)],"x52": [("x42",16),("x62",3),("x51",4),("x53",4)],"x53": [("x43",3),("x63",5),("x52",7)],"x54": [("x44",2),("x64",1),("x53",4),("x55",1)],"x55": [("x45",19),("x65",0)],
    "x61": [("x51",4),("x62",3)],"x62": [("x52",7),("x61",4),("x63",5)],"x63": [("x53",4),("x62",3),("x64",1)],"x64": [("x63",5),("x65",0)],"x65": [("x55",1),("x64",1)]
}

allaHuristic = lambda state, problem : heuristicAlla(state,problem)
startFinish = [("x11","x35"),("x35","x31"),("x31","x65")]
solution=[]

problemx = problem(graph=newGraph,startPoint="x11",goalPoint="x35",is_trace=True, maxFound=1)
solution += search.breadthfirstsearch(problemx)
#print(solution)

problemx = problem(graph=newGraph,startPoint="x35",goalPoint="x31",is_trace=False, maxFound=1)
solution = solution[:-1] + search.uniformCostSearch(problemx)
#print(solution)

problemx = problem(graph=newGraph,startPoint="x31",goalPoint="x65",is_trace=False, maxFound=1)
solution = solution[:-1] + search.aStarSearch(problemx,allaHuristic)
print(solution)