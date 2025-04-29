import random

def play(game=None):
  
  symbols = ['🍒',' 🍇', '🍉',  '7️⃣']
  
  results = random.choices(symbols, k=3)
  
  print(f"{results[0]} | {results[1]} | {results[2]}")
  
  win = results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣"

  if win:
    print("Jackpot! 💰")

  else:
    print("Thanks for playing!")


keep_playing = "Y"

while keep_playing.upper != 'N':
  play()
  keep_playing = input("Do you want to keep playing? Y/N:")
