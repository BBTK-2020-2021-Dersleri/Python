x=8
for i in range(0, 5): 
    for j in range(0,x): 
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    x=x-2
    print()