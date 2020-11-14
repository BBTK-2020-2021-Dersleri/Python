# Hesap makinesi
print("Enter 1 for addition")
print("Enter 2 for subtact")
print("Enter 3 for division")
print("---------------------------------")
first=int(input("Enter a first number:"))
second=int(input("Enter a second number:"))
secenek=int(input("Seceneğinizi giriniz: "))
if(secenek==1):
    sum=first+second
    print("Sum:",sum)

elif(secenek==2):
    subt=first-second
    print(subt)
    
elif(secenek==3):
    div=first/second
    print(div)

else:
    print("You can enter just 1-2-3")