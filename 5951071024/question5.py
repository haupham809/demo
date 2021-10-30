list1=[2, 3, 4, 5, 6, 7, 8]
list2=[4, 9, 16, 25, 36, 49, 64]
print(list1)
print(list2)
result={}
for i in list1:
    count=dict({i:i*i})
    if i*i  in list2:
        result.update(count)
print(result)