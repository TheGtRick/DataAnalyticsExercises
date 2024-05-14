file = open('Assigment 3\\bear.txt', 'r')
a = file.readlines()
n = 0
for i in a:
    n += 1
    i.strip()
print(n)