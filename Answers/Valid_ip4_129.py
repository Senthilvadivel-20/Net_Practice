'''
Auth : Senthil
Date : 10/07/2023
'''


ip = input('Enter IP4 address: ')

def check(ip):
    ip = ip.split('.')
    if len(ip) == 4:
        ip = [int(i) for i in ip]
        for i in ip:
            if (255 < i) or (i < 0):
                return False
        return True
    return False
    


print(check(ip))