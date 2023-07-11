'''
Auth : Senthil
Date : 11/07/2023

Question: 70. Write a function to count the number of trailing zeros in the factorial of a given number.

'''


n = input('Enter the float number: ')

def trail_zero(n):
    n = (n.split('.'))[1]
    c = 0
    for i in n:
        if i == "0":
            c+=1
        elif  i != "0":
            break
    return c

print(trail_zero(n))