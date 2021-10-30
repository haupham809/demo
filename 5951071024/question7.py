firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
def checkset(a,b):
    n=0
    for i in a:
        if i in b :
          n=n+1
    return n==len(a)
def supercheskset(a,b):
    n=0
    for i in a:
        if i in b :
          n=n+1
    if not checkset(a,b) and n<len(b):
        return False
    elif checkset(a,b):
        return True


print("First set is subset of second set -"+ str(checkset(firstSet,secondSet)))
print("Second set is subset of First set -"+ str(checkset(secondSet,firstSet)))
print("First set is super set of second set -"+ str(supercheskset(firstSet,secondSet)))
print("Second set is Super set of First set -"+ str(supercheskset(secondSet,firstSet)))


if checkset(firstSet,secondSet):
        firstSet={}
if checkset(secondSet,firstSet):
    secondSet={}

print(firstSet)
print(secondSet)