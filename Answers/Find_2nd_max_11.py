'''
Auth: Senthil
Date: 24/07/2023

'''

# arr = [int(i) for i in (input("Enter the Array: ")).split(',')]


arr =  [-2, -5, -1, -9, -3]

larg = float('-inf')
second_larg = float('-inf')

for i in arr:
    if i > larg:
        second_larg = larg
        larg = i
    elif i > second_larg and i != larg:
        second_larg = i

        


print(larg)
print(second_larg)


