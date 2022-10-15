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


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('Количество паролей?'+ "\n")
length = input('Длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)