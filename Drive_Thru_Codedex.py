def get_item(order):
  if order == 1:
    return "🍔 Cheeseburger"
  elif order == 2:
    return "🍟 Fries"
  elif order == 3:
    return "🥤 Soda"
  elif order == 4:
    return "🍦 Ice Cream"
  elif order == 5:
    return "🍪 Cookie"
  else:
    return "Unavaliable"

def welcome():
  print("Welcome to Hamburglar's!")
  print("1. 🍔 Cheeseburger")
  print("2. 🍟 Fries")
  print("3. 🥤 Soda")
  print("4. 🍦 Ice Cream")
  print("5. 🍪 Cookie")

welcome()

option = int(input("What would you like to order? "))
print(get_item(option))