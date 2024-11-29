from csp import csp
constraints={
    "x1,x2": lambda arr: arr[0]!=arr[1],
    "x1,x3": lambda arr: arr[0]!=arr[1],
    "x2,x3": lambda arr: arr[0]!=arr[1],
    "x4,x3": lambda arr: arr[0]!=arr[1],
    "x4,x2": lambda arr: arr[0]!=arr[1],
    #"x4,x1": lambda arr: arr[0]!=arr[1],
}

csp_obj = csp({"x1","x2","x3","x4"},{1,2,3},constraints=constraints)

result=csp_obj.backtrackingSearch()

print(result)