# To Create a variable amount of layers and choose the best possible one, i need to generate all combinations first 
# For Example : For 4 nodes, there are 5 possible layers:
# 1 1 1 1 : Four layers, each with one 
# 1 1 2   : 3 layers
# 1 3     : 2 Layers
# 2 2     : 2 Layers == Best Solution ==
# 4       : 1 Layer

from itertools import combinations

def combineStrings(a,b):
    if len(b):
        solution=[]
    else:
        return a
    for x in a:
        for y in b:
            solution.append(f"{x},{y}")
    return solution
#returns [(x,y,z)....] 
def combination_alla(n, max_layer):
    if max_layer == 0:
        return []
    solutions = []
    for i in range(1,n+1):
        probset=[f"{i}"]
        prev=combination_alla(n-i,max_layer-1)
        if len(prev) == 0 and i != n: continue
        combs = combineStrings(probset,prev)
        for sol in combs:
            solutions.append( sol )
    return solutions

solveit=combination_alla(40,max_layer=4)
for i in solveit:
    for item in i:
        print(f"{item}",end=" ")
    print()