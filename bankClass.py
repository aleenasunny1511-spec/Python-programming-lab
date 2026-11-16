#Create a bank account with members: account number,name,type of account,&balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class Bank:
     def __init__(self,accNo,name,accType,balance=0):
         self.accNo=accNo
         self.name=name
         self.accType=accType
         self.balance=balance
     def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit successfull ! New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Enter a positive value")
     def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(" New balance: {self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdraw amount. Enter a positive value")


     def display(self):
        print("\nAccount Number: ",self.accNo)
        print("\nAccount Holder Name: ",self.name)
        print("\nAccount Type: ",self.accType)
        print("\nAccount Balance: ",self.balance)
b1=Bank(1002,"Nidhi","Savings",0)
b1.display()
while True:
    print("\nMENU***")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Display")
    print("4.Exit")
    choice=int(input("\nEnter your choice(1-4): "))
    if choice==1:
        d=float(input("\nEnter amount to be deposited: "))
        b1.deposit(d)
    elif choice==2:
        w=float(input("\nEnter amount to  Withdraw: "))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("Exit")
        break
    else:
        print("Enter a valid choice.")
        
               
               
            
