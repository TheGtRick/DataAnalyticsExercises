def FallingRange(a, b, c):
    for i in range(a, b + 1):
        if i == c:
            return True
    return False
a = int(input("Start of Your range: "))
b = int(input("End of Your range: "))
c = int(input("Your Number: "))
print(FallingRange(a, b, c))