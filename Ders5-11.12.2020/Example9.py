def Rectangle(a,b):
    area=a*b
    circumference=2*(a+b)
    print("Rectangle area formula--> a.b")
    print("Rectangle cicumference formula--> 2.(a+b)")
    print("-----Result-----")
    print("Area {} , Cicumference: {}".format(area,circumference))
    print()
    
def Square(a):
    area=a**2
    circumference=4*a
    print("Square area formula--> a²")
    print("Square cicumference formula--> 4.a")
    print("-----Result-----")
    print("Area {} , Cicumference: {}".format(area,circumference))
    print()
    
def Cylinder(r,h):
    area=2*3*r*(r+h)
    V=3*(r**2)*h
    print("Cylinder area formula--> 2.pi.r.(r+h)")
    print("Cylinder volume formula--> pi.r².h")
    print("-----Result-----")
    print("Area {} , V: {}".format(area,V))
    print()
    
def Menu():
    while(1):  
        print("Enter 1 for square calculations:")
        print("Enter 2 for rectangle calculations:")
        print("Enter 3 for cylinder calculations:")
        print("Enter q for quit:")
        choose=input()
        if(choose=="1"):
            edge=int(input("Enter edge:"))
            Square(edge)
        elif(choose=="2"):
            shortEdge=int(input("Enter short edge:"))
            longEdge=int(input("Enter long edge:"))
            Rectangle(shortEdge,longEdge)
        elif(choose=="3"):
            r=int(input("Enter radius:"))
            h=int(input("Enter h:"))
            Cylinder(r,h)
        elif(choose=="q"):
            print("Goodbye...")
            print(":)")
            break
        else:
            print("OOOPS!")

            
            
Menu()