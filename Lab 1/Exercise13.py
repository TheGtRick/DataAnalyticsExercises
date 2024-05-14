def factorial(a):
    b = 1
    for i in range(1, a + 1):
        b = b * i
    return b
a = int(input("Enter the number: "))
print(factorial(a))