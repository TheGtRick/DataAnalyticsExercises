def maxOfThree(a, b, c):
    d = max(max(a, b), c)
    return d
a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))
print(maxOfThree(a, b, c))