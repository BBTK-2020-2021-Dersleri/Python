a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if(a>b and a>c):
    max=a
    print("First one is the greatest. Number is:",max)
elif(b>a and b>c):
    max=b
    print("Second one is the greatest. Number is:",max)
else:
    max=c
    print("Third one is the greatest. Number is:",max) 
