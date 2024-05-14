import math
a = int(input("Enter Your Score: "))
b = ["F", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]
if a < 50:
    print("F")
else:
    print(b[math.floor((a - 50) / 5) + 1])