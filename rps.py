import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("Enter...\n\t1 for Stone\n\t2 for paper\n\t3 for Scissors:\n")
print((playerchoice))

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3 !") # program na tym etapie przestaje dzialac

computerchoice = random.choice("123") # python wybiera liczbe 1 2 lub 3

computer = int(computerchoice) # zmieniamy jej tyo zeby mozna bylo napisac logike

print("")
# dodajemy stale z enuma aby wyswietlane byly wartosci dla poszczegolnych cyfr
print("Your chose " + str(RPS(player)).replace("RPS.", "")+ ".")
print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("You win😍")
elif player == 2 and computer == 1:
    print("You win😍!")
elif player == 3 and computer == 2:
    print("You win😍!")
elif player == computer:
    print("Tie game!")
else:
    print("Computer wins🤔")