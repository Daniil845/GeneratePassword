import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
login_number = input('Количество логинов?'+ "\n")
login_length = input('Длин логина?'+ "\n")
login_number = int(login_number)
login_length = int(login_length)
for n in range(login_number):
    login = ''
    for i in range(login_length):
        login += random.choice(chars)
        print(login)
