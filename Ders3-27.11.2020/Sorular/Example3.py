num=int(input("Enter number: "))
digit=0
temp=num
while(temp>0):
    basamakSayisi=temp%10
    digit=digit+1
    temp=temp//10
    
lastDigit  = num % 10
firstDigit = (num // pow(10, digit-1)) 

swap= lastDigit 
swap = swap *pow(10,digit-1)   
swap =swap + num % (pow(10, digit-1)) 
swap =swap- lastDigit  
swap = swap+firstDigit
print(swap)