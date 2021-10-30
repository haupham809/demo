def fun():
    for s in range(10):
        if s==0:
            print(("Current Number "+str(0)+" Previous Number"+str(s)+ "sum :{} + {} ={}").format(s,s,s+s)   )
        else :
            print(("Current Number "+str(s-1)+" Previous Number "+str(s)+ " sum :{} + {} ={}").format(s-1,s,s+s-1)   )
        
fun()