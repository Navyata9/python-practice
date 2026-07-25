import random
playing= True
number= str(random.randint(0,9))

print("I will print a number from 0 to 9 and you will have to guess the number one digit at a time")
print("The game ends when you get one hero")

while playing:
    guess= input("give me your best guess: \n")
    if number==guess:
        print("You win the game!")
        print("the number was", number)
        break

    else:
        print("Your guess wasnt quite right, try again \n")
                 