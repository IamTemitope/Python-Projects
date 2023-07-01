print("Welcome To Number Guessing Game")

try:
    name = input('What is your name: ')

    import random

    number = random.randrange(1, 100)

    number_guesses = 0

    while True:
        guess = int(input("Guess a number between 1 - 100: "))

        number_guesses += 1

        if guess == number:
            print('Congratulations', name, 'you guessed after', number_guesses, 'attempts')
            break

        if guess < number:
            print('Try again! Your guess is low')
        else:
            print('Try again! Your guess is high')
except:
    print(name, "Try inputting a valid command")
