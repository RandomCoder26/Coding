#Made By RandomCoder

import random

chars = "\\`1234567890-=qweryuiop[]asdfghjkl;zxcvbnm,./"

try:
    str(print('Password Generator.'))
    password_length = int(input('Enter Password Length: '))

    password = '\033[34m'

    for i in range(password_length):
        password += random.choice(chars)

    str(print(f'Your Password Is: {password}'))

    print('\033[0m')

except:
    str(print('You Entered An Invalid Length For Your Password!'))