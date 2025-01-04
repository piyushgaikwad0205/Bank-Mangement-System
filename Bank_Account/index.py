from functions import innerBank
from functions import getAccountInfo

class CreateUser :

        userName = "admin"
        userAccNo = getAccountInfo('AccountNumber')
        userBalance = getAccountInfo('Balance')
        userPassword = getAccountInfo('Password')
 

        def getAccountNo (self):
                return self.userAccNo
        def getAccountBalance (self):
                return self.userBalance
        def getAccountPass (self):
                return self.userPassword


# ------------------------------------------Main Program-------------------------------------------------

NewUser = CreateUser()
count = 0
exitbox = False
proseed = False
key = True
# print(type(NewUser.userName))
# print(type(NewUser.userPassword))
while (key):
        
        tempName = input("Enter User Name : ")
        tempPass = input("Enter the Password : ")

        if((tempName == NewUser.userName and int(tempPass) == int(NewUser.userPassword ))):
                
                print("\nWELCOME TO USERS DASHBORAD....\n")
                key = False
                proseed = True
        
        elif(count >= 5):
                
                print("Limits has been Reached Please Try Again Later...")
                exitbox = True
                key = False
        else :
                print("Wrong User Name or Password...")
                count = count + 1
                print(count)
                print("Try Again...\n")



if(exitbox):
        print("Thank You for Banking With Us .... ")
        print("Please Try again Later!!")


if(proseed):
        
        passkey = True
        userInput = None
        while(passkey):

                userval = "Press 1 For Credit Money\nPress 2 Debit Money\nPress 3 Check Balance\nPress 4 for Forget"
                print(userval)
                try:
                        userInput = int(input("Enter User choise : "))
                        passkey = not(innerBank(userInput))
                        proseed = True
                        
                except (TypeError):
                        
                        print("Enter the Wrong Input... Try Again\n")
                        passkey = True
                
                if (not (userInput <= 4)and (userInput > 0)):
                        passkey = True
