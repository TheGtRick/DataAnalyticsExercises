a = "*"
b = 2
for i in range(1, 10):
    if(i < 6):
        for j in range(0, i):
            print(a, end="")
    else:
        for j in range(i - b, 0, -1):
            print(a, end="")
        b = b + 2
    print()
