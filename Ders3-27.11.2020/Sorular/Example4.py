sign=1
sum=0
for i in range(1,10+1):
    sum=sum+(sign/(i**2)) 
    sign=sign*-1
    
print(sum)