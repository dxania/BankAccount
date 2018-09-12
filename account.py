class BankAccount:
    
    global dictt 
    dictt = [{'Name':'daizy','PIN':'1234','Balance':1000}, {'Name':'keem','PIN':'2345','Balance':2000}]

    def __init__(self,balance):
        self.balance=balance
        print("Press: 1 for Account opening")
        print("       2 for Balance Check")
        print("       3 for Cash Deposit")
        print("       4 for Cash Withdraw")
        print("       5 for Account Closure")

        option = int(input("Select Transaction: "))
        if option == 1:
            self.openAcc(self, self, self)
        elif option == 2:
            self.get_balance(self, self, self)
        elif option == 3:
            self.deposit(self,self, self, self)
        elif option == 4:
            self.withdraw(self,self,self, self)
        elif option == 5:
            self.closeAcc(self,self)
        else:
            print("Please choose an option from the list")


    def openAcc(self, name, pin, balance):

        details = []
        self.name = name
        self.pin = pin
        self.balance = 0
        name = raw_input("Enter your name: ")
        pin = raw_input("Enter your PIN: ")
        details.append(name)
        details.append(pin)
        details.append(self.balance)
        print(name + ", these are your details:" )
        print(details)
        print("You are welcome to OBBank")
    

    def get_balance(self, name, pin, balance):
                
        self.name = name
        self.pin = pin
        name = raw_input("Enter your name: ")
        pin = raw_input("Enter your PIN: ")

        for item in dictt:
            if item["Name"] == name and item["PIN"] == pin:
                print("Your balance is", item["Balance"])
            # else:
            #     print("Please enter valid credentials")


    def deposit(self,amount,name, pin, balance):
        self.name = name
        self.pin = pin
        self.amount = amount
        self.balance = balance
        name = raw_input("Enter your name: ")
        pin = raw_input("Enter your PIN: ")
        
        for item in dictt:
            if item["Name"] == name and item["PIN"] == pin:
                
                amount = input("Enter amount to deposit: ")
                balance = item["Balance"]
                balance+= amount
                print("You have deposited " + str(amount) + ". " + "Your new balance is " +  str(balance))

    def withdraw(self,amount,name, pin, balance):
        self.name = name
        self.pin = pin
        self.amount = amount
        self.balance = balance
        name = raw_input("Enter your name: ")
        pin = raw_input("Enter your PIN: ")
        
        for item in dictt:
            if item["Name"] == name and item["PIN"] == pin:
                balance = item["Balance"]
                amount = input("Enter amount to withdraw: ")
                if balance > amount:
                    balance-=amount
                    print("You have withdrawn " + str(amount) + ". " + "Your new balance is " +  str(balance))
                else:
                    print("You do not have sufficient balance to complete this transaction")

    def closeAcc(self,name,pin):
        self.name = name
        self.pin = pin
        name = raw_input("Enter your name: ")
        pin = raw_input("Enter your PIN: ")
            
        for item in dictt:
            if item["Name"] == name and item["PIN"] == pin:
                print (item)
                print("Are you sure you want to close this account?")
                print("1 for YES")
                print("2 for No")

                option = int(input("Select Transaction: "))
                if option == 1:
                    del item
                    # del dictt[item]
                    # list.remove(item)
                    print(dictt)
                elif option == 2:
                    print("Your account is still active")
                else:
                    print("Please choose an option from the list")
                   
    
def main():
    one = BankAccount(0)
    # try:
    #     one = Bank(0)
    # except:
    #     print("No instances defined")


if __name__ == "__main__":
    main()

