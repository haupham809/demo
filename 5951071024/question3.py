list=[50, 51, 52, 53, 54, 55, 56, 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69,70, 71, 72, 73, 74]
list1=list[0:(len(list)-1)//3]
list2=list[(len(list)-1)//3:2*((len(list)-1)//3)]
list3=list[2*((len(list)-1)//3):]
print("\nlist :"+str(list)
)
print("\nlist 1: " +str(list1))
list1.reverse()
print("\nrever each list 1 : " +str(list1))

print("\nlist 2 :"+str(list2))
list2.reverse()
print("\nrever each list 2 :" +str(list2))

print("\nlist 3 :"+str(list3))
list3.reverse()
print("\nrever each list 3 : " +str(list3))
