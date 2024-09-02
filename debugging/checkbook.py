#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        """
        Initialize the Checkbook with a balance of $0.00.

        Function Description:
        Sets up the Checkbook instance with an initial balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the Checkbook.

        Parameters:
        amount (float): The amount of money to deposit.
        
        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the Checkbook.

        Parameters:
        amount (float): The amount of money to withdraw.
        
        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the Checkbook.

        Parameters:
        None
        
        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook.

    Function Description:
    Provides a command-line interface for users to deposit, withdraw, or check their balance.
    Handles user input and performs the requested actions.
    
    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
