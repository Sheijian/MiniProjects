import random

print(" ---------------------")
print("| Rock Paper Scissors |")
print(" ---------------------")

rps = ["R", "P", "S"]

score = 0
kiscore = 0
i = 1

chance = int(input("How many time you want to play?: "))

while i <= chance:
    computerchoise = str(random.choice(rps))
    userchoice = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
    if userchoice == computerchoise:
        print("Tie You Both Entered Same")
    elif userchoice == "R":
        print("Computer Enter: ", computerchoise)
        if computerchoise == "P":
            print(" You lose! Paper covers Rock")
            kiscore += 1
        else:
            print(" You win! Rock smashes Scissors")
            score += 1
    elif userchoice == "P":
        print("Computer Enter: ", computerchoise)
        if computerchoise == "S":
            print(" You lose! Scissor cut Paper")
            kiscore += 1
        else:
            print(" You win! Paper covers Rock")
            score += 1
    elif userchoice == "S":
        print("Computer Enter: ", computerchoise)
        if computerchoise == "R":
            print("👉 You lose! Rock smashes Scissors")
            kiscore += 1
        else:
            print("👉 You win! Scissor cut Paper")
            score += 1
    else:
        print(":(")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {score} | Computer: {kiscore}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")
    i += 1

print("\n\n##### Game Over #####")
print("*******************************************")
if score < kiscore:
    print(
        " Sorry you lost the game \n computer has won the game with score:", kiscore
    )
elif score == kiscore:
    print(" Game is Tie Play Again ")
else:
    print(" You won the Game with score:", score)
