import random

number = random.randint(1, 100)
count = 1
chance = 10

while 1 <= chance:
    num = int(eval(input("Guess the Number: ")))
    if num > number:
        print("Your guess was too high: Guess a number lower than", num)
    elif num < number:
        print("Your guess was too low: Guess a number higher than", num)
    else:
        print("You Win!")
        print("guesses you took:", count)
        break

    chance -= 1
    print(chance, "Guesses left")
    count += 1
    print()

print("Game over!")
print(" The number is:", number)
