class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"Your balance is currently £{self.balance}")

current_account = BankAccount("Pika", "Chu", 12345678, "Current", 1234, 100.00)

current_account.deposit(96)

current_account.display_balance()

current_account.withdraw(25)

current_account.display_balance()

# testing...

#class BankAccount:
    #def __init__(self, balance):
        #self.balance = balance
        
    #def display_balance(self):
        #print(f"Your balance is currently £{self.balance}")

# test account
#test_account = BankAccount(100.00)

# Check if this prints
#print("Testing print statement...")

# Try to display balance
#test_account.display_balance()

# Print something after to check execution flow
#print("Code execution completed.")

