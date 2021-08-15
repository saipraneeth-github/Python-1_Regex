r = 4
lst = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
copy = lst

m=(2*r)-2

count = 0

for i in range(0,r+1):
    for j in range(0,m):
        print(end=" ")
    m = m-1
    
    for j in range(0,i+1):
        count = count+1
        if(j!=0):
            print(lst[count-1], end =" ")
        else:
            print(lst[count-1], end =" ")
    print("\n")
