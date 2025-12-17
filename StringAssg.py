# 1st Question
s = input("Enter: ")
v = c = d = sp = 0
for i in s:
    if i.isalpha():
        if i.lower() in 'aeiou':
            v += 1
        else:
            c += 1
    elif i.isdigit():
        d += 1
    else:
        sp += 1
print("Vow:", v)
print("Con:", c)
print("Dig:", d)
print("S_C:", sp)

# 2nd Question
a = input("Enter: ")
words = a.split()
result = []
for word in words:
    result.append(word[::-1])
print(" ".join(result))

# 3rd Question
b = input("Enter: ")
if b == b[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4th Question
j = input("Enter: ")
freq = {}
for ch in j:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for m, o in freq.items():
    print(m, ":", o)

# 5th Question
f = "Mohit"
try:
    f[0] = 'z'
except TypeError as e:
    print("Error:", e)


