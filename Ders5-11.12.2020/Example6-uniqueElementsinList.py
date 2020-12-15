list1=[1,1,2,2,3,1,4,5,6]
unique=[]
def uniqueNumber(liste):
    for i in liste:
        if i not in unique:
            unique.append(i)
            
    return unique

print(uniqueNumber(list1))