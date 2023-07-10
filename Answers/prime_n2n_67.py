'''
Auth: Senthil
Date: 04/07/2023
'''


m = [2,3,5,7,11,13]

def prime(n):
    for i in m:
        if (n % i) == 0:
            return False
    return True

# print(prime(89))

st = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))

for i in range(st,en+1):
    if prime(i):
        print(i,end=", ")