# EXAMPLE 3
# Denklem kökleri bulma
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
delta=(b**2)-(4*a*c)
birinci_kök = (-b - (delta ** 0.5)) / (2*a)
ikinci_kök = (-b + (delta ** 0.5)) /(2*a)
print("First roof: ",birinci_kök)
print("Second roof: ",ikinci_kök)