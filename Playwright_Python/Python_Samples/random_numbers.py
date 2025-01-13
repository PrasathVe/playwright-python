import random

inp = int(input("Guess the Random Number between 1 to 5: "))
rand = random.randrange(1,5)

if (inp==rand):
    print("Wow.You Guess it Right!")
else:
    print("Wrong. Try Again")
