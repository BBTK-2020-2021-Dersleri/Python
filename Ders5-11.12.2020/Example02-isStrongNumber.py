def factorial(kalan):
    fact = 1
    for i in range(1,kalan+1):
        fact = fact * i
    return fact

def isStrongNumber(number):
    toplam=0
    temp = number
    while(temp !=0):
        kalan = temp % 10
        temp = temp // 10
        toplam = toplam + factorial(kalan)
    if(toplam == number):
        return True
    else:
        return False        

number = int(input("Enter a number: "))
for i in range(1,number):
    if(isStrongNumber(i)):
        print(i)