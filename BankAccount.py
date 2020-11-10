class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self.full_name = full_name
        #Randomly generated 8 digit number, unique per account.
        self.account_number = account_number
        #9 digit number, this number is the same for all accounts.
        self.routing_number = routing_number
        #The balance of money in the account, should start at 0.
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Amount Deposited: $" + str(amount) )

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
        else:
            print("Insufficient funds.")
            self.balance -= 10

    def get_balance(self):   
        print(f"Your current balance is: ${self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest


    def print_receipt(self):
        print(self.full_name)
        print("Account No.: ****" + str(self.account_number)[4:])
        print("Routing No.: " + str(self.routing_number))
        print("Balance: $" + str(self.balance))

Account1 = BankAccount("Alexander Lopez",19471347,205214952,0.0)
Account2 = BankAccount("Jeff Bezos",13471947,205214952,0.0)
Account3 = BankAccount("Elon Musk",13321921,205214952,0.0)

Account1.print_receipt()
Account1.deposit(1000000)
Account1.withdraw(100)
Account1.print_receipt()



