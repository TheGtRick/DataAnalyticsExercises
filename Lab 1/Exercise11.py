b = int(input("Enter the number of elements in list: "))
c = 0
for i in range(b):
    a = int(input("Eneter the number: "))
    if a % 2 == 0:
        c += 1
print("Odd elements: " + str(b - c) + " Even elements: " + str(c))