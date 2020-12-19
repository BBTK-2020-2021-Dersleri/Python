number = int(input("Enter a number: "))
def isPrime(number):
    if(number==1):
        return False
    for i in range (2,number):
        if(number%i==0):
            return False
    return True
    
if(isPrime(number)):
    print("Prime Number.")
else:
    print("Not Prime!")