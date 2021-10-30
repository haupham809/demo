set1={65, 42, 78, 83, 23, 57, 29}
set2 ={67, 73, 43, 48, 83, 57, 29}
for i in set2:
    if i in set1:
        set1.remove(i)
print(set1)