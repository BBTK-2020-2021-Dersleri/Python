score=float(input("Enter a score:"))

if((score)>=0.0 and (score)<=1):
    if((score)>=0.9):
        print("A")
    elif((score)>=0.8):
        print("B")
    elif((score)>=0.7):
        print("C")
    elif((score)>=0.6):
        print("D")
    else:
        print("Bad score")
else:
    print("Bad score")