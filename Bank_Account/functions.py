# ----------------------------Libaries---------------------------------------------------------------

from datetime import datetime


# get Account Info 
# -------------------------------------------------------------------------------------------
def getAccountInfo(n):
        with open('Bank_Account\\txts\\bankProfile.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if n == 'AccountNumber' and 'Account_Number' in line:
                        accountNumber = line.split('=')[1]
                        return accountNumber
                    elif n == 'Balance' and 'BankBalance' in line:
                        bankBalance = line.split('=')[1].strip()
                        return bankBalance
                    elif n == 'Password' and 'Password' in line:
                        password = line.split('=')[1].strip()
                        return password
                    elif n == 'UserName' and 'User_name' in line:
                        userName = line.split('=')[1].strip()
                        return userName
                
        return "User Parameter Not Found"


# -------------------------------Update Bank Balance Funtion------------------------------------------------------------


def updateBankBalance (newBalance):

        with open('Bank_Account\\txts\\bankProfile.txt','r') as file:
              lines = file.readlines()
        
        with open('Bank_Account\\txts\\bankProfile.txt','w') as file:
              for line in lines:
                    if 'BankBalance' in line:
                          file.write(f'BankBalance = {newBalance}\n')
                    else:
                          file.write(line)
        
# -----------------------------------------Debit--------------------------------------------------


def Debit(amount):

        bankBalance = getBalance()
        # print(type(bankBalance), type(amount))
        newbal = float(bankBalance-amount)
        if (amount < bankBalance):
                updateBankBalance(newbal)
                return sucessfull()+f'New Balance = {getAccountInfo('Balance')}'
        else:
              
            return "Uneffienct Bank Balance"+ f"Current Bank Balance = {getAccountInfo('Balance')}"


# --------------------------------------Creadit-----------------------------------------------------

def Credit(amount):

        bankBalance = getAccountInfo('Balance')
        newbal = float(bankBalance) + amount
        updateBankBalance(newbal)
        return sucessfull()+f"New Balance = {getBalance()}"


# --------------------------------------GET Balance-----------------------------------------------------

def getBalance ():
        amount = getAccountInfo('Balance')
        return float(amount)
                            
# --------------------------------------GET User Name-----------------------------------------------------


def getUserName ():
            userName = getAccountInfo('UserName')
            return userName


# --------------------------------------Messages-----------------------------------------------------

def sucessfull():
        return("\nTransaction was Compelet Successfully...\n")    

def unscessfull():
        return("\nTransaction could not be Procced...")  
                    

# ----------------------------------------Oprations---------------------------------------------------

def innerBank(opp):
       
    if (opp == int(1)):
          
          amount = float(input("Enter the Amount : "))
          print(Credit(amount))
          creditEntry(amount)
          return True
    elif (opp == 2):
          
          amount = float(input("Enter the Amount : "))
          print(Debit(amount))
          debitEntry(amount)
          return True
    elif (opp == 3):
          
          print(f"Your Bank Balance is : {getBalance()}")
          return True
    
    elif (opp == 4):
          print("Log Out ScuessFull....")
          print("exitig...")
          return True
    
    elif (opp == 5):
          
          bol = admin()
          return bol
                   
        
    return False


# ----------------------------------------opration at Statements--------------------------------------------------

def creditEntry (amount):
      
      with open('Bank_Account\\txts\\satement.txt','a+') as file:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            
            file.write(f"|{current_time} |     {amount}    |               | {getBalance()}        |\n")


   

def debitEntry (amount):
            with open('Bank_Account\\txts\\satement.txt','a+') as file: 
                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  
                    file.write(f"|{current_time} |               |     {amount}    | {getBalance()}        |\n")

# -----------------------------------------Admin Opreation-------------------------------------------------

def admin():
        key = True
        option = "\nPress 1 for Change User Name \nPress 2 for Change Password"
        choise = None
        while (key):
                key = False
                try:
                    print(option) 
                    choise = int(input("Enter you Choise : "))
                    if (not (choise == 1 or choise == 2)):
                          print("Wrong Input... Try Again....")
                          key = True

                except (TypeError and ValueError):
                    print("Wrong Input... Try Again")
                    key = True
       
        if (choise == 1):
                changeUserName()
                print("User Name Changed Sucessfully...")
                return True
                
        elif(choise == 2):
                changePassword()
                print("Passwrod change Sucessfully...")
                return True
                


            
      



def changePassword ():
       
        newPassword = input("\nEnter New Password : ")

        with open('Bank_Account\\txts\\bankProfile.txt','r') as file:
             
             lines = file.readlines()

        with open('Bank_Account\\txts\\bankProfile.txt','w') as file:
             
             for line in lines:
                    if 'Password' in line:
                         file.write(f'Password = {newPassword}\n')
                    else :
                          file.write(line)




                    
def changeUserName():
    newUserName = input("\nEnter New user Name : ")

    with open('Bank_Account\\txts\\bankProfile.txt', 'r') as file:
        lines = file.readlines()
        # print("lines",lines)

    with open('Bank_Account\\txts\\bankProfile.txt', 'w') as file:
        for line in lines:
            # print("line in loop"+line)
            if 'User_name' in line:
                file.write(f'User_name = {newUserName}\n')
            else:
                file.write(line)


# -----------------------------------------Main-------------------------------------------------

if __name__ == "__main__":
        
        # print(Debit(100))
        # creditEntry(100)
        # changeUserName()
        # changePassword()
        admin()
        pass