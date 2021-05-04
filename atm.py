class Atm: 
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self): 
        print("Your Balance Is: $500")
    def withdraw(self,amount): 
        newAmount=500-amount
        print("New Balance: ",newAmount)
def main(): 
    cardNumber=input("Enter The Card Number: ")
    pinNumber=input("Enter The Pin Number: ")
    user=Atm(cardNumber,pinNumber)
    print("Choose Your Activity: ")
    print("1. Balance Inquiry 2. Withdraw")
    activity=int(input("Enter Your Activity Number: "))
    if(activity==1): 
        user.checkBalance()
    elif(activity==2): 
        amount=int(input("Enter The Amount for Withdrawl: "))
        user.withdraw(amount)
    else: 
        print("Please Enter the Right Number.")
if __name__=="__main__":
    main()