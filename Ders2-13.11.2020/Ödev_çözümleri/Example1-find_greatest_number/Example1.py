a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if(a>b):
    if(a>c):
        max=a
        print("First one is the greatest. Number is:",max)
    else:
        max=c
        print("Third one is the greatest. Number is:",max)
else:
    if(b>c):
        max=b
        print("Second one is the greatest. Number is:",max)
    else:
        max=c
        print("Third one is the greatest. Number is:",max)
