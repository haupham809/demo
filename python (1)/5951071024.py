import math

print("Ten :Pham Thanh Hau")
print("MSV:5951071024")

print("sline 1")
x = 34 - 23 # A comment.

y ='Hello' # Another one.

z = 3.45

if z == 3.45 or y == 'Hello':

    x = x + 1

    y = y + ' World' # String concat.

print (x)

print (y)


print("sline 2 Exercise 1")
Annie=25
Ellie=21
print(str(Annie)+"-"+str(Ellie)+"="+str(Annie-Ellie))


a=14.99
b=27.95
c=19.83
d=a+b+c
print(str(a)+"$+"+str(b)+"$+"+str(c)+"$="+str(d)+"$")


print(20*15)

print(2**10)

print("min(3, 1, 8, -2, 5, -3)="+str(min([3, 1, 8, -2, 5, -3])))

print(3 == 4-2)

print("The value of 17//5 is 3 "+str(17//5 == 3))

print("The value of 17%5 is 3 "+str(17%5 == 3))

print("284 is even "+str(284%2 ==0))

print("284 is even and 284 is divisible by 3 "+str(284 %2 ==0 and 284 %3 == 0))

print("284 is even or 284 is divisible by 3 "+str(284 /2==0 or 284 %3 ==0))


print("sline 2 Exercise 2")

s1="good"
s2="bad"
s3="silly"
print ("s1="+str(s1))
print ("s2="+str(s2))
print ("s3="+str(s3))

print(" ' ' in s1 "+str(' ' in s1))

print(" ' ' in s2 "+str(' ' in s2))

print(" ' ' in s3 "+str(' ' in s3))

s4=s1+s2+s3
print (" ' ' in s1+s2+s3  " +str(' ' in s4) )

print("the concatenation of 10 copiesof s3 is " +str(10*s3))

print("sline 2 Exercise 3")
s='abcdefgh'
print("s[0] ="+str(s[0]))
print("s[2] ="+str(s[2]))
print("s[7] ="+str(s[7]))
print("s[-1] ="+str(s[-1]))
print("s[-3] ="+str(s[-3]))

print("sline 2 Exercise 4")
lst = [159.99, 160.00, 205.95,128.83, 175.49]

lst.append(160.00)
print("Compute the number of retailers selling the boots for $160.00 : "+ str(lst.count(160.00)))
print("Find the minimum price in lst : "+ str(min(lst)))
print("find the index of the minimum price in list lst : "+ str(lst.index(min(lst))))
lst.remove(min(lst))
print("remove the minimum price from list lst : "+ str(lst))
lst.sort()
print("Sort list lst in increasing order : "+ str(lst))


print("sline 2 Exercise 5")

print("The length of the hypotenuse in a right triangle whose other two sides have lengths 3 and 4 :"+ str(math.sqrt(3**2+4**2)))
print("The value of the Boolean expression that evaluates whether the length of the above hypotenuse is 5 :"+str(math.sqrt(3**2+4**2) == 5 ))

print("The area of a disk of radius 10 :"+str(math.pi*10**2) )

print("The value of the Boolean expressionthat checks whether a point withcoordinates (5, 5) is inside a circlewith center (0,0) and radius 7 :"+str((2*5**2 < 7**2)) )


