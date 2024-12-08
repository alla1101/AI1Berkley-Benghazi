from csp import csp
import math
constraints={
    "x1,x2": lambda arr: arr[0]!=arr[1] and abs(arr[0] - arr[1]) !=1,
    "x1,x3": lambda arr: arr[0]!=arr[1]  and abs(arr[0] - arr[1]) != 2,
    "x2,x3": lambda arr: arr[0]!=arr[1] and abs(arr[0] - arr[1]) != 1,
    "x4,x3": lambda arr: arr[0]!=arr[1]  and abs(arr[0] - arr[1]) != 1,
    "x4,x2": lambda arr: arr[0]!=arr[1]  and abs(arr[0] - arr[1]) !=2,
    "x4,x1": lambda arr: arr[0]!=arr[1]  and abs(arr[0] - arr[1]) != 3,

}

csp_obj = csp({"x1","x2","x3","x4"},{1,2,3,4},constraints=constraints)

result=csp_obj.backtrackingSearch()

print(result)