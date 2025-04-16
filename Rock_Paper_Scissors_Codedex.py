#Rock, Paper, Scissors

print("Rock, Paper, Scissors")

print("1) 👊")

print("2) ✋")

print("3) ✌️")

import random

#rock = "👊"

#paper = "✋"

#scissors = "✌️"

while True:
  player = input("Pick a number:")
  if player == "1":
    print("You chose: 👊")
  elif player == "2":
    print("You chose: ✋")
  elif player == "3":
    print("You chose: ✌️")
  else:
    print("Error")
  break

computer = random.randint (1, 3)

if computer == 1:
  print("Computer chose: 👊")
elif computer == 2:
  print("Computer chose: ✋")
elif computer == 3:
  print("Computer chose: ✌️")
else:
  print("Error")

#paper beats rock
if player == "1" and computer == 2:
  print("Computer wins!")
#paper beats rock
elif player == "2" and computer == 1:
  print("You win!")
#rock beats scissors
elif player == "1" and computer == 3:
  print("You win!")
#rock beats scissors
elif player == "3" and computer == 1:
  print("Computer wins!")
#scissors beat paper
elif player == "3" and computer == 2:
  print("You win!")
#scissors beat paper
elif player == "2" and computer == 3:
  print("Computer wins!")
#it's a tie
else:
  print("It's a tie!")
