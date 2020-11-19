class BankAccount:
    #Bank Account Object Initialization
    def __init__(self,full_name,account_number,routing_number,balance):
        self.full_name = full_name
        #Randomly generated 8 digit number, unique per account.
        self.account_number = account_number
        #9 digit number, this number is the same for all accounts.
        self.routing_number = routing_number
        #The balance of money in the account, should start at 0.
        self.balance = 0
        self.balance = balance

    #Bank Account Methods
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

    def chargeATMFee(self):
        self.balance -= 3

#Three Example Bank Accounts
Account1 = BankAccount("Alexander Lopez",19471347,205214952,0.0)
Account2 = BankAccount("Jeff Bezos",13471947,205214952,0.0)
Account3 = BankAccount("Elon Musk",13321921,205214952,0.0)

#Encapsulation Through putting them in a collective list. 
AccountsAvailable = [Account1, Account2, Account3]

#Testing of the First Bank Account
Account1.print_receipt()
Account1.deposit(1000000)
Account1.withdraw(100)
Account1.add_interest()
Account1.print_receipt()

#Loop for Terminal ATM Interface
while True:
    print("__________________________________________")
    print("Welcome to your Digital Bank ATM Terminal")
    userNumber = input("There are three accounts available. Please select number from 0 to 2: ")
    if userNumber in ["0","1","2"]:
        action = input("Choose Input: (1) Get Balance. (2) Deposit. (3) Withdraw. ")
        if action == str(1):
            print (AccountsAvailable[int(userNumber)].print_receipt())
        elif action == str(2):
            deposit = input("Please enter your amount to deposit: ")
            print (AccountsAvailable[int(userNumber)].deposit(int(deposit)))
        elif action == str(3):
            withdraw = input("Please enter your amount to withdraw (Fee is $3): ")
            print (AccountsAvailable[int(userNumber)].withdraw(int(withdraw)))
        elif action == "Exit":
            break
        else:
            print("Please select one of the following options")
    else:
        print("Input for Account Not Recognized. Please Try Again ")