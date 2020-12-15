n=int(input("Enter n: "))
if(n<0 or n>168): #if n is outside of range display invalid massage
    print("Invalid.")
else:
    if(n>=0 and n<=40):
        n=n*8
    elif(n>40 and n<=50): #40 saatten fazla her çalışmaya 9 ile çarptık.
        n=(40*8)+(n-40)*9
    elif(n>=50):
        n=(40*8)+(10*9)+(n-50)*10 #50 saatten fazla her çalışmaya 10 ile çarptık.
      
print("YOU MADE {} DOLLAR THIS WEEK".format(n))