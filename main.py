# Project: Guess the Number!

# The program should generate a random number between 0 and 100. The player then needs to guess what that number is.

# Should the user guess wrong, the program should respond by telling them their guess is either too low or too high. When the user guesses right, your program should ask them if they want to play again.

# For a little added challenge, you can limit the number of guesses to 5, for example.
# (required library "random")

#code:
i = 1
while i > 0:
    import random
    a = random.randint(0, 100)
    print('you will have only 5 chances to guess ')
    chance = 0
    while chance < 5:
        guess = int(input("enter the number:"))
        if guess > a:
            print(f"you are too high, u can try again in {4-chance} chances")
        elif guess < a:
            print(f"you are too low, u can try again in {4-chance} chances")
        elif guess == a:
            print("Ohh yeah! You got it")
            cont = input(
                "enter 'yes' if u wanna play again \n else enter 'no' to exit:"
            )
            if cont == 'no':
                break
            if cont == 'yes':
                i = 1
                break
        chance += 1
        if chance == 5:
            print('you are out of chances. sorry!')
        i = 0
#End.
