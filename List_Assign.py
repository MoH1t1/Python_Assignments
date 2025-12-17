# 1st Question
l = [1,9,8,7,6,4,8]
new = []
for i in l:
    if i not in new:
        new.append(i)
print(new)

# 2nd Question
l1 = [2,4,6,7,8,9]
e=[]
for i in l1:
    if i %2 ==0:
        e.append(i)
print(e)

# 3rd Question
l2 = [5, 6, 7, 8, 9]
la = se = float('-inf')
for i in l2:
    if i > la:
        se = la
        la = i
    elif i > se and i != la:
        se = i
print(se)

# 4th Question
n = [[5,6,7], [11,23,45]]
for i in n:
    print(sum(i))

# 5th Question
import copy
o = [[1,2], [9,7]]
s = copy.copy(o)
d = copy.deepcopy(o)
o[0][0] = 99
print("Original:", o)
print("Shallow Copy:", s)
print("Deep Copy:", d)

















