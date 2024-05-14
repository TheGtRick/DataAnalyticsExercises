file = open('Assigment 3\\bear.txt', 'r')
a = file.readlines()
n = 0
for i in a:
    if n == 2 or n == 3:
        print(i.strip())
    else:
        i.strip()
    n += 1