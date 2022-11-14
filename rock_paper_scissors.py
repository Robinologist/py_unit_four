import random


def who_wins(userchoice, computerchoice):
    if userchoice == computerchoice:
        return "Tie!"
    if userchoice == 1 and computerchoice == 2:
        return "You Lost! (Paper beats Rock)"
    if userchoice == 1 and computerchoice == 3:
        return "You Win! (Rock beats Scissors)"
    if userchoice == 2 and computerchoice == 1:
        return "You Win! (Paper beats Rock)"
    if userchoice == 2 and computerchoice == 3:
        return "You Lost! (Scissors beats Paper)"
    if userchoice == 3 and computerchoice == 2:
        return "You Won! (Scissors beats Paper)"
    if userchoice == 3 and computerchoice == 1:
        return "You Lost! (Rock beats Scissors)"


def main():
    userchoice = input("Please enter your choice!\n1:Rock 2:Paper 3:Scissors\n")
    computerchoice = (random.randint(1, 3))
    print("your choice:", userchoice)
    print("computer choice:", computerchoice)
    print(who_wins(userchoice, computerchoice))


if __name__ == '__main__':
    main()
