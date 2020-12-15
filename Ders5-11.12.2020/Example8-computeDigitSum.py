n=int(input("Enter n:"))
def digit_sum(n): #fonksiyon oluşturuldu
    sum=0
    if(n<0):
        n=n*(-1) #pozitif sayıya çevirdik
    while(n>0):
        kalan=n%10
        sum=sum+kalan 
        n=n//10 
    return sum #basamak toplamını return et

print(digit_sum(n))