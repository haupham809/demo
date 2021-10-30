def check(a,b):
    if(a*b>1000):
        return a+b;
    elif(a*b<1000):
        return a*b;
while True:
    try:
        a=int(input("nhap so thu nhat :"))
        b=int(input("nhap so thu hai :"))
        print(check(a,b))
        break;
    except:
        print("nhap khong dung vui long nhap lai")
