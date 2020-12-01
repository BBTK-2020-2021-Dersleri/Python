for i in range(1, 5+1) : 
    for j in range(1, 5+1) : 
        if (i == 1 or i == 5 or
            j == 1 or j == 5) : 
            print("*",end="")             
        else : 
            print(" ", end="")                  
    print(" ")