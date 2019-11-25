import quiz

users = [
    
]

def login(username, password):
    return username == "ICYLGR01" and password == "Cocoban123"
    # om username är ICYLGR01 och lösenordet är Cocoban123 returnera True, annars returnera False

login_in = True
while login:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if login(username, password):
         print("Welcome", username, ", You may now progress to the quiz \n") # du lyckades
         quiz.start()  
    else:
        print("Incorrect")
        login_in = True
        # startas om

    # if username == "ICYLGR01":
    #     password = input("Enter your password:")
    #     if password == "Cocoban123":
    #         print("Welcome", username, ", You may now progress to the quiz \n")
            
    #     if password != "Cocoban123":
    #         password_again = input("Incorrect password. Would you like to try to login again? Yes or no?")
    #         if password_again.lower() == "yes":
    #             login = True
    #         if password_again.lower() == "no": 
    #             quit()
            
    # else:
    #     username_again = input("Username incorrect. Would you like to try again? Yes or no?")
    #     if username_again.lower() == "yes":
    #         login = True
    #     if username_again.lower() == "no":
    #         print("Thank you for trying, welcome back later!")
    #         quit()                                                                                                                      

