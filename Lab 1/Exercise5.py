a = int(input("Enter Units: "))
if a <= 100:
    print(0)
elif a > 100 and a <= 200:
    print(a * 5)
else:
    print((a - 200) * 15 + 100 * 5)