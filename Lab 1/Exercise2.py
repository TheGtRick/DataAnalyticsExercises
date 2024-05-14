a = input("Enter your string: ")
b = a[0]
a = a[1:len(a)].replace(b.lower(), "$")
a = b + a[0:len(a)].replace(b.upper(), "$")
print(a)