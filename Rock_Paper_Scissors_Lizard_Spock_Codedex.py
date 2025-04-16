#Rock, Paper, Scissors, Lizard, Spock

print("Rock, Paper, Scissors, Lizard, Spock")

print("1) 👊")

print("2) ✋")

print("3) ✌️")

print("4) 🦎")

print("5) 🖖")

import random

#rock = "👊"

#paper = "✋"

#scissors = "✌️"

#lizard = "🦎"

#spock = "🖖"

while True:
  player = input("Pick a number:")
  if player == "1":
    print("You chose: 👊")
  elif player == "2":
    print("You chose: ✋")
  elif player == "3":
    print("You chose: ✌️")
  elif player == "4":
    print("You chose: 🦎")
  elif player == "5":
    print("You chose: 🖖")
  else:
    print("Error")
  break

computer = random.randint (1, 5)

if computer == 1:
  print("Computer chose: 👊")
elif computer == 2:
  print("Computer chose: ✋")
elif computer == 3:
  print("Computer chose: ✌️")
elif computer == 4:
  print("Computer chose: 🦎")
elif computer == 5:
  print("Computer chose: 🖖")
else:
  print("Error")

#paper covers rock
if player == "2" and computer == 1:
  print("You win!")
elif player == "1" and computer == 2:
  print("Computer Wins!")
#rock breaks scissors
elif player == "1" and computer == 3:
  print("You win!")
elif player == "3" and computer == 1:
  print("Computer wins!")
#scissors cut paper
elif player == "3" and computer == 2:
  print("You win!")
elif player == "2" and computer == 3:
  print("Computer wins!")
#rock crushes lizard
elif player == "1" and computer == 4:
  print("You win!")
elif player == "4" and computer == 1:
  print("Computer wins!")
#lizard poisons spock
elif player == "4" and computer == 5:
  print("You win!")
elif player == "5" and computer == 4:
  print("Computer wins!")
#spock smashes scissors
elif player == "5" and computer == 3:
  print("You win!")
elif player == "3" and computer == 5:
  print("Computer wins!")
#scissors beat lizard
elif player == "3" and computer == 4:
  print("You win!")
elif player == "4" and computer == 3:
  print("Computer wins!")
#lizard eats paper
elif player == "4" and computer == 2:
  print("You win!")
elif player == "2" and computer == 4:
  print("Computer wins!")
#paper disproves spock
elif player == "2" and computer == 5:
  print("You win!")
elif player == "5" and computer == 2:
  print("Computer wins!")
#spock vaporises rock
elif player == "5" and computer == 1:
  print("You win!")
elif player == "1" and computer == 5:
  print("Computer wins!")
#it's a tie
else:
  print("It's a tie!")
