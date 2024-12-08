from csp import csp
constraints={
    "q1,q2": lambda arr: arr[0]!=arr[1] and abs(arr[0]-arr[1])!=1,
    "q1,q3": lambda arr: arr[0]!=arr[1],
    "q2,q3": lambda arr: arr[0]!=arr[1],
    "q4,q3": lambda arr: arr[0]!=arr[1],
    "q4,q2": lambda arr: arr[0]!=arr[1],
    "q4,q1": lambda arr: arr[0]!=arr[1],
}

csp_obj = csp({"q1","q2","q3","q4"},{1,2,3,4},constraints=constraints)

result=csp_obj.backtrackingSearch()

print(result)