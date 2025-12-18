# 1st Question
import csv
file = open("attendance.csv", "w", newline="")
w = csv.writer(file)
w.writerow(["ID", "Name","Department", "Status"])
w.writerow([101, "Mohit","IT" ,"Present"])
w.writerow([102, "Ayushi","Marketing", "Absent"])
file.close()
print("File created")

# 2nd Question
file = open("attendance.csv", "r")
reader = csv.reader(file)
for i in reader:
    print(i)
file.close()

# 3rd Question
file = open("attendance.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow([103, "Divyanshu","Marketing", "Absent"])
file.close()
print("Added")

# 4th Question
file = open("attendance.csv", "r")
r = csv.reader(file)
count = 0
next(r)
for i in r:
    if i[3] == "Absent":
        count += 1
file.close()
print("Total Absent:", count)

# 5th Question
emp_id = input("Enter ID: ")
file = open("attendance.csv", "r")
r = csv.reader(file)
found = False
next(r)
for i in r:
    if i[0] == emp_id:
        print("Emp-found:", i)
        found = True
        break
if not found:
    print("Emp NF")
file.close()