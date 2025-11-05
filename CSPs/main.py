from csp import csp
N = 25
domain={i for i in range(1,N+1)}
variables = {f"q{i}" for i in range(1,N+1)}
constraintx={}
for i in range(1,N+1):
    for j in range(1,N+1):
        if j==i: continue
        x_t=f"q{i},q{j}"
        d= abs(i-j)
        x_k=lambda arr,b=d: arr[0]!=arr[1] and abs(arr[0] - arr[1]) != b
        constraintx.update({x_t:x_k})

csp_obj = csp(variables,domain,constraints=constraintx)
result=csp_obj.backtrackingSearch()
print(result)
