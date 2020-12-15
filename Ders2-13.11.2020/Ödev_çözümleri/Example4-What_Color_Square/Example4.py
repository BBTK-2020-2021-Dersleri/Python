col,row=input("Enter col and row:")
if(col=='a' or col=='c' or col=='e' or col=='g'):
    if((int(row))%2==0):
        print("White square.")
    else:
        print("Black square")
else:
    
     if((int(row))%2==0):
        print("Black square.")
    
     else:
        print("White square")