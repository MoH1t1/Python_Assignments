# 1st Question
file = open("students.txt", "w")
file.write("001, Mohit, 90, Sports\n")
file.write("002, Lalit, 74, Non-sports\n")
file.write("003, Atharva, 34,Non-sports\n")
file.close()
print("Student records written successfully")

# 2nd Question
file = open("students.txt", "r")
data = file.read()
print(data)
file.close()

# 3rd Question
file = open("students.txt", "a")
file.write("004, Sangita, 68,Non-sports\n")
file.close()
print("Added")

# 4th Question
file = open("students.txt", "r")
c = 0
for i in file:
    c = c+ 1
file.close()
print("Total student records:", c)

# 5th Question
name = input("Enter Name: ").strip()
file = open("students.txt", "r")
found = False
for i in file:
    if name in i:
        print("Stud found:", i)
        found = True
        break
if not found:
    print("Stud NF")
file.close()




















