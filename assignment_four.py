import random

playerScore=0
computerScore=0
winCode=0
playerStanding=0

def playerTurn():
    global playerStanding
    if playerStanding != 1:
        playerChoice = int(input("Please enter your choice!\n1:Hit 2:Stand\n"))
    if playerChoice == 1:
        newPlayerCard()
        computerTurn()
    elif playerChoice == 2:
        print("Okay you'll stop here")
        playerStanding=1
        computerTurn()

def computerTurn():
    global computerScore
    if computerScore <= 15:
        print("The dealer Hit")
        computerScore = computerScore + (random.randint(1, 13))
        print("The dealer's new score is", computerScore)
    else:
        print("The dealer is standing")

def newPlayerCard():
    global playerScore
    print("Here's your new card:")
    card=(random.randint(1, 13))
    playerScore = playerScore + card
    print("You got",card,"your new score is",playerScore)

def evaluateScore():
    winCode = 0
    if playerScore == 21:
        winCode = 1
    elif computerScore == 21:
        winCode = 2
    elif playerScore > 21:
        winCode = 3
    elif computerScore > 21:
        winCode = 4
    return winCode

def main():
    playerTurn()
    if evaluateScore() == 1:
        print("You Win! (You got 21)")
    elif evaluateScore() == 2:
        print("You Lose! (Computer got 21)")
    elif evaluateScore() == 3:
        print("You Lose! (You went over 21)")
    elif evaluateScore() == 4:
        print("You Win! (Computer went over 21)")
    elif evaluateScore() == 0:
        print("Next Turn!")
        main()

main()