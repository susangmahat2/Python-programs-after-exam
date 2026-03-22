import random
while True:

    useraction=input("Enter your action (rock, paper, scissors): ")
    actions=["rock","paper","scissors"]
    computeraction=random.choice(actions)
    print(f"\nYou chose {useraction}, computer chose {computeraction}.")
    
    if useraction==computeraction:
        print("It's a tie!")
    elif useraction=="rock":
        if computeraction=="scissors":
            print("You win!")
        else:
            print("You lose!")
    elif useraction=="paper":
        if computeraction=="rock":
            print("You win!")
        else:
            print("You lose!")
    elif useraction=="scissors":
        if computeraction=="paper":
            print("You win!")
        else:
            print("You lose!") 
    playagain=input("Do you want to play again? (yes/no): ")
    if playagain.lower()!="yes":
        print("Thanks for playing!")
        break 


