sign=1
sum=0
for i in range(1,40+1,2):
    sum=sum+(sign/i)
    sign=sign*-1
print(sum)