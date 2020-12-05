n=int(input("Enter upper value: "))
for num in range(1,n):
    basamak=0
    toplam=0
    temp=num
    temp2=num

    while(temp>0):
        temp=temp//10
        basamak+=1
        
    while(temp2>0):
        digit = temp2%10
        toplam=toplam+(digit**basamak)
        temp2=temp2//10
        
    if(num==toplam):
        print(toplam)