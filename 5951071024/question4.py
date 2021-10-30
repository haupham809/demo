list=[1,23,1,4,34,12,23,23,44,12,34,567,7834,789345,789,45678]
print(list)
result={}
for i in list:
    count=dict({i:list.count(i)})
    if i not in result.keys():
        result.update({i:list.count(i)})
print(result)