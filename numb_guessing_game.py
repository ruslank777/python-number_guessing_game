import random

n = random.randrange(1, 10)
guess = int(input("Set a number: "))
while n!=guess:
    if guess < n:
        print("Too cold")
        guess = int(input("Try to set number again: "))
    elif guess > n:
        print("Too hot!")
        guess = int(input("Try to set number again: "))
    else:
        break

print('you guessed it')