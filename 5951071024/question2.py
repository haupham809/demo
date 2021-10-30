
list1=[1,"giao thong ",5,12,"123",323,"giao thong ",123,2,"hau"]
print(list1)
i =list1[1]
list1=list1[0:1]+list1[2:]
list1.insert(3,i)
list1.append(i)
print(list1)


