file = open('Assigment 3\\bear.txt', 'r')
a = file.read()
b = a.split(' ')
c = ''
for i in b:
    if len(c) < len(i):
        c = i
print(c)