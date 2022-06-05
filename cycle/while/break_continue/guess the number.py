import random

number = random.randint(0, 100)
print(number)
max_tries = 4
tries = 0

while tries < max_tries:
    guess = int(input('Input integer: '))
    if guess < number:
        print('number > than guess')
    elif guess > number:
        print('number < than guess')
    else:
        print('You win')
        break
    tries += 1

if tries >= max_tries:
    print('You lose')

