number_of_terms=int(input("Enter n: "))
sum=0
start=2
for i in range(0,number_of_terms):
    print(start, end=" ")
    sum += start
    start = (start * 10) + 2

print("Toplam-->",sum)