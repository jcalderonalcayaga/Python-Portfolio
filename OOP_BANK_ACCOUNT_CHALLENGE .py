#Object Oriented Programming Challenge
#For this challenge, create a bank account class that has two attributes:

#owner
#balance

#and two methods:

#deposit
#withdraw

#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account Owner: {self.owner} \nAccount Balance: {self.balance}'
    def deposit(self,dep_amnt):
        self.balance += dep_amnt
        print(f'Deposit of {dep_amnt} was approved. Have a great day.')
    def withdrawal(self,withd_amnt):
        if self.balance >= withd_amnt:
            self.balance -= withd_amnt
            print(f'Withdrawal of {withd_amnt} was approved. Have a great day.')
        else:
            print('ERROR. Please contact your local branch. (999) 999-999. Thank you.')

acct1 = Account('John Doe', 6000)
print(acct1) #PRINTS ACCOUNT DETAILS
acct1.owner #PRINTS ACCOUNT OWNER ONLY
acct1.balance #PRINTS ACCOUNT BALANCE ONLY
acct1.deposit(1000) #DEPOSITS MONEY INTO ACCOUNT
acct1.withdrawal(7000) #WITHDRAWS ALL MONEY FROM ACCOUNT 
acct1.withdrawal(1) #OVERDRAWN TRANSACTION. ERROR MESSAGE EXPECTED
