# 1st Question
def even_list(l):
    r = []
    for num in l:
        if num % 2 == 0:
            r.append(num)
    return r
a=[1,2,3,4,5]
print(even_list(a))

# 2nd Question
def char_count(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
b= "mohitt"
print(char_count(b))

# 3rd Question
def pali(n):
    s = str(n)
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False
c= int(input("Enter: "))
print(pali(c))

# 4th Question
def avg(*args):
    t = 0
    for i in args:
        t += i
    average = t / len(args)
    return average

print(avg(1,2,3))

# 5th Question
def com_elements(l1, l2):
    l3 = []
    for i in l1:
        if i in l2:
            if i not in l3:
                l3.append(i)
    return l3
x=[1,2,3,4,5]
y=[4,5,6,7,8]
print(com_elements(x,y))