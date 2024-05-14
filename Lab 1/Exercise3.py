a = input("First String: ")
b = input("Second String: ")
c = a
a, b = a.replace(a[0:2], b[0:2]), b.replace(b[0:2], a[0:2])
print(a + " " + b)