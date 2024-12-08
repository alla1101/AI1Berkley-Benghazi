# init Parameters
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

moves=[(-1,0),(1,0),(0,-1),(0,1)]
for i in range(1,7):
    for j in range(1,6):
        print(f"\"x{i}{j}\":","{[",end="")
        ending= True
        for t,k in moves:
            if matrixA[i+t][j+k] == 'r':
                continue
            if ending:
                ending = False
            else:
                print(",",end="")
            print(f"(\"x{i+t}{j+k}\",{matrixA[i+t][j+k]})",end="")

        print("]},",end="")
    print()
