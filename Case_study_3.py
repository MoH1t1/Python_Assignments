# 1st Question
file = open("sales.txt", "w")
file.write("Laptop, Electronics, 55450, 11\n")
file.write("Mobile, Electronics, 22500, 25\n")
file.write("Headphone, Accessories, 3570, 51\n")
file.close()
print("File created")

# 2nd Question
file = open("sales.txt", "a")
file.write("Watch, Accessories, 6700, 89\n")
file.close()
print("Added")

# 3rd Question
import csv
txt_file = open("sales.txt", "r")
csv_file = open("sales.csv", "w", newline="")
w = csv.writer(csv_file)
w.writerow(["Product", "Category", "Amount","Quantity"])
for l in txt_file:
    data = l.strip().split(", ")
    w.writerow(data)
txt_file.close()
csv_file.close()
print("Conversion Done")

# 4th Question
file = open("sales.csv", "r")
reader = csv.reader(file)
for i in reader:
    print(i)
file.close()

# 5th Question
total = 0
with open("sales.csv", "r", newline="") as file:
    r = csv.reader(file)
    header = next(r)
    for line_no, row in enumerate(r, start=2):
        if not row or len(row) < 4:
            continue
        price = float(row[2])
        quantity = int(row[3])
        total += price * quantity
print("Total Sales Amount:", total)



