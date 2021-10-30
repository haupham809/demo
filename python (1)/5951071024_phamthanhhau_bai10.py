def fun():
    result=[]
    list_one=[12,21,32,45,120]
    list_two=[1,22,2,11,150,17]
    for s in list_one:
        if s%2!=0:
            result.append(s)
    for s in list_two:
        if s%2==0:
            result.append(s)
    return result
print(fun())