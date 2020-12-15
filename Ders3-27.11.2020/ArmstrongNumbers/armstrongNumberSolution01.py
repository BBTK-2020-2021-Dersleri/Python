n=int(input("Enter upper value: "))
for num in range(1,n):
    basamak=0
    toplam=0
    temp=num
    
    basamak=len(str(num))
     
    while(temp>0):
        digit = temp%10
        toplam=toplam+(digit**basamak)
        temp=temp//10
        
    if(num==toplam):
        print(toplam)