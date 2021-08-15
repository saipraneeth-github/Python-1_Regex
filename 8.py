def circularly_identical(list1, list2):
      
    list3 = list1 * 2
      
    for x in range(0, len(list1)):
        z = 0 
 
        for y in range(x, x + len(list1)):
            if list2[z]== list3[y]:
                z+= 1
            else:
                break

        if z == len(list1):
            return True 
      
    return False
          
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [10, 0, 10, 0, 10]

if(circularly_identical(list1, list2)):
    print("Identical")
else:
    print("Not Identical")

if(circularly_identical(list2, list3)):
    print("Identical")
else:
    print("Not Identical")
