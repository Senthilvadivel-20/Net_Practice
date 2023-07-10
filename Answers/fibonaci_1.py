'''
Auth : Senthil
'''

st = [0,1]

def ind(n):
    if n > 2:
        for i in range(n-2):
            st.append(sum(st[-2:]))

    return st[:n]


print(ind(2))