def fun(n):
    rev = 0
    o = n
    while n>0:
        rem = n % 10
        rev = rem + (rev*10)
        n = int(n / 10)
    if n==rev:
        print("\n" +str(o)+ " (Original) = " +str(rev)+ " (Reverse)")
    else:
        print("\n" +str(o)+ " (Original) != " +str(rev)+ " (Reverse)")
      
fun(50)