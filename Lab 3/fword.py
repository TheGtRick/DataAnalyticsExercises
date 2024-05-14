file = open('Assigment 3\\bear.txt', 'r')
a = file.read()
b = a.split()
c = 0
d = []
for i in b:
    if i not in d:
        d.append(i)
        print(i + ': ', end='')
        for j in b:
            if i == j:
                c += 1
        print(c)
        c = 0