# script for password generation

import random


# characters available to use in the password

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMMNOPQRSTUVWXYZ0123456789!@#$%^&*-_[]{}=+'

# amount of passwords to be generated with the int being the amount provided by the user

amount = input('How many passwords? - ')
amount = int(amount)

# how long the password should be according to the user, the int is also the length provided by the user

length = input('How long should the password be? - ')
length = int(length)

# for the certain amount of times a password will be created using a random choice of the provided characters above

for i in range(amount):
    password = ''
    for o in range(length):
        password += random.choice(char)
    print(password)