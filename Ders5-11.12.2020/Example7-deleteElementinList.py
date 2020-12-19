liste1=[10,20,30,40,50]
liste2=[]
index=int(input("Enter index that you want to delete number:"))
if(index!=1):
    for i in liste1[0:index-1]:
        liste2.append(i)
    for i in liste1[index:5]:
        liste2.append(i)
else:
    for i in liste1[index:5]:
        liste2.append(i)
    
print(liste2)