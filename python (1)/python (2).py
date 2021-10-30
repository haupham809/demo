def findstr(s,chuoi):
    result=[]
    start=0
    while True:
        if chuoi.find(s,start)==-1:
            break
        
            
        elif chuoi.find(s,start)!=-1:
            result.append(chuoi.find(s,start))
            start=chuoi.find(s,start)+len(s)
    return result
print (findstr("Emma",'Emma is name of the Emma Emma'))