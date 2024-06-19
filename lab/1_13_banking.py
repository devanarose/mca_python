class Account:

  def __init__(self, account_number, balance=0):
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):

    if amount > 0:
      self.balance += amount
      print(f"Deposit successful. New balance: {self.balance:.2f}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):

    if amount > 0 and self.balance >= amount:
      self.balance -= amount
      print(f"Withdrawal successful. New balance: {self.balance:.2f}")
    else:
      print("Insufficient funds or invalid withdrawal amount.")

  def get_balance(self):

    return self.balance

class SavingsAccount(Account):

  def __init__(self, account_number, interest_rate, balance=0):
    super().__init__(account_number, balance)  # Call base class constructor
    self.interest_rate = interest_rate

  def calculate_interest(self):

    interest = self.balance * self.interest_rate
    return interest

  def apply_interest(self):
    interest = self.calculate_interest()
    self.balance += interest
    print(f"Interest earned: {interest:.2f}. New balance: {self.balance:.2f}")

def main():
  # Create a savings account object
  account_number = input("Enter your account number: ")
  interest_rate = float(input("Enter the interest rate (e.g., 0.05 for 5%): "))
  savings_account = SavingsAccount(account_number, interest_rate)

  while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      amount = float(input("Enter amount to deposit: "))
      savings_account.deposit(amount)
    elif choice == '2':
      amount = float(input("Enter amount to withdraw: "))
      savings_account.withdraw(amount)
    elif choice == '3':
      balance = savings_account.get_balance()
      print(f"Your account balance is: {balance:.2f}")
    elif choice == '4':
      savings_account.apply_interest()
    elif choice == '5':
      print("Exiting program.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()
