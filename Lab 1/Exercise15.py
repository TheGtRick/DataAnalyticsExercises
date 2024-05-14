def uniqueElements(a = []):
    b = []
    for i in range(len(a)):
        if a[i] not in b: b.append(a[i])
    return b
a = [1, 3, 2, 5, 2, 3, 5, 5, 4, 5, 1]
print(uniqueElements(a))