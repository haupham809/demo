def checklist():
    listnumber=[1.5,3,5,10,1,24,15,40]
    result=[]
    for i in listnumber :
        if i%5==0:
            result.append(i)
    return result
print(checklist())