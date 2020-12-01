rows=int(input("Enter rows: "))
space = 2 * rows - 2
star=1
for i in range(0, rows):
    for j in range(0, space):
        print(end=" ")
    space = space - 1
    for j in range(0,star):
        print("*", end="")
    star=star+2
    print("")
    
space = rows 
star=rows*2-3
for i in range(rows, -1, -1):
    for j in range(space, 0, -1):
        print(end=" ")
    space = space + 1
    for j in range(0,star):
        print("*", end="")
    star=star-2
    print("")