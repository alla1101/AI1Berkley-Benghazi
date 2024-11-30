# To Create a variable amount of layers and choose the best possible one, i need to generate all combinations first 
# For Example : For 4 nodes, there are 5 possible layers:
# 1 1 1 1 : Four layers, each with one 
# 1 1 2   : 3 layers
# 1 3     : 2 Layers
# 2 2     : 2 Layers == Best Solution ... maybe lol ==
# 4       : 1 Layer

def combineStrings(a,b):
    if len(b):
        solution=[]
    else:
        return a
    for x in a:
        for y in b:
            solution.append((f"{x},{y}").replace(" ",""))
    return solution

def combination_alla(n,max_layer,max_node):
    if max_layer == 0:
        return []
    solutions = []
    for i in range(1,max_node):
        probset=[f"{i}"]
        prev=combination_alla(n-i,max_layer-1,max_node)
        if ( len(prev) == 0 and i != n): continue  
        # If Max Layer was Reached, then ProbSet won't get us to the required amount of layers, so we move to the next i.
        combs = combineStrings(probset,prev)
        for sol in combs:
            solutions.append( sol )
    return solutions

number_of_nodes = 26
max_number_of_node_per_layer = 5

solveit=combination_alla(number_of_nodes,max_layer=8,max_node=max_number_of_node_per_layer)
for i in solveit:
    arr=i.split(",")
    end_ch=""
    for item in arr:
        print(end_ch+str(int(item)),end="")
        end_ch=","
    print()