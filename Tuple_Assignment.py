# 1st Question
t = (1,2,3,4,5)
ma= t[0]
mi = t[0]
for i in t:
    if i > ma:
        ma = i
    if i < mi:
        mi = i
print("Max:", ma)
print("Min:", mi)

# 2nd Question
l = [(5, 'M'), (2, 'O'), (3, 'H')]
d = {}
for i, j in l:
    d[i] = j
print(d)

# 3rd Question
t = (9,8,7,6,5,6)
k = int(input("Enter a number: "))
count = 0
for i in t:
    if i == k:
        count += 1
print("Occ:", count)

# 4th question
t1 = ([1, 2, 3],)
t1[0][0] = 9
print(t1)

# 5th Question
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1
print("t1:", t1)
print("t2:", t2)









