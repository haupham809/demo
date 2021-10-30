
list1=[1,2,5,12,234,323,456,123,65]
list2=[45,23,46,234,567,3456,567,234,567,2345]
result=[]
for i in list1:
    if i%2!=0:
        result.append(i)
for i in list2:
    if i%2==0:
        result.append(i)
print("list 3 :"+str(result))

