A = {1,2,3,4}
B = {1,2,7,8}
print("U:", A | B)
print("I:", A & B)
print("Dif:", A - B)
print("SD:", A ^ B)

A1 = {1,2,3,4}
B1 = {3,4,5,9}
A1 = A1 - B1
B1 = B1 - A1
print("Set A:", A1)
# print("Set B:", B1)

A = {1,2}
B = {1,2,3, 4}
if A.issubset(B):
    print("A is subset of B")
else:
    print("A is not subset of B")

s = {1,2,3,4,5}
n = int(input("Ente limit: "))
for i in s:
    if i > n:
        print(i)


l3 = [1,2,3,4,5,6,54,3]
u_s =  set(l3)
print(u_s)
u_l = list(u_s)
print(u_l)



