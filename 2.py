def walls(l,b,n,m):
    print("cost of each painting is 120 per square meter")
    wallone =120*float(l)*float(b)
    walltwo =120*float(n)*float(m)
    total = wallone + walltwo
    print("The cost of painting  wall-1 is:%.2f" %(wallone))
    print( "The cost of painting wall-2 is :%.2f" %( walltwo))
    print("The total cost is :%.2f" %(total))
l= input("Enter the length  of wall-1:")
b=input("Enter the  breath of wall-1:")
n= input("Enter the length of wall-2:")
m=input("Enter the  breath of wall-2:")
walls(l,b,n,m)
