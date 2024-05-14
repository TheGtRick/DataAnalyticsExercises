import math
def isPrime(a = 0):
    if a == 2: return True
    elif a == 1 or a == 0: return False
    else:
        b = round(math.sqrt(a))
        c = 0
        d = 0
        for i in range(2, b + 1):
            if isPrime(i):
                c += 1
                if a%i != 0:
                    d += 1
        if c == d: return True
        else: return False
a = int(input())
print(isPrime(a))