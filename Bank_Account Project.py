"""This is a simple excercise demonstrating classes and objects. It is modeled after a bank account. The methods included are: accepting deposits and withdrawls, showing the balance, and showing the name of the account. Included are checks to make sure that funds are available in the account before they can be removed."""

# Set up the class and member variable. 
class BankAccount(object):
  balance = 0
  def __init__(self, name): 
    self.name = name
  def __repr__(self): 
    return "This account belongs to %s. The account balance is %02d. " % (self.name, self.balance)
  
  # Defining actionable functions. 
  def show_balance(self): 
    print(("Account balance: %02d") % (self.balance))
  def deposit(self, amount): 
    if amount <= 0: 
      print("Error. Deposits must be greater or equal to 0.")
    else: 
      print(("Deposit Amount: %02d") % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount): 
    self.amount = amount
    if amount > self.balance: 
      print("Error. You do not have enough money in your account to withdrawl that amount.")
    else:
      print(("Withdrawl Amount:  %02d") % (amount))
      self.balance -= amount
      self.show_balance()
       
#Define an object
my_account = BankAccount("Kristin")

#Printing the balance could be accomplished any of these 3 ways:
print(my_account)
print(my_account.__repr__())
my_account.show_balance()

#Test out the deposit and withdraw functions. Print output to verify. 
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account.__repr__())
