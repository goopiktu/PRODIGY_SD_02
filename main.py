import random

# generate number

# user guess

# computer checks 
## computer says higher or lower 
## -> go back to user guess till gets it right


## bot should say "Generating random number"
## "number generated"
## "guess a number from n-n"
##

def generateNumber(): 
    return random.randint(1,10)



def main():
    computerNumber = generateNumber()
    userGuess = -99999
    guessCounter = 0

    while userGuess != computerNumber:
        userGuess = int(input("Guess: "))
        guessCounter+=1
        if computerNumber < userGuess:
            print("Too High")
        elif computerNumber > userGuess:
            print("Too Low")
        else:
            print(f"YOU GUESSED IT it's {computerNumber}")
            print(f"{guessCounter} ATTEMPTS")

            
main()