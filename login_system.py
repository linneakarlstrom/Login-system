import quiz
login = True
while login:
    username = input("Enter your username:")
    if username == "ICYLGR01":
        password = input("Enter your password:")
        if password == "Cocoban123":
            print("Welcome", username, ", You may now progress to the quiz \n")
            quiz.start()
            
        if password != "Cocoban123":
            password_again = input("Incorrect password. Would you like to try to login again? Yes or no?")
            if password_again.lower() == "yes":
                login = True
            if password_again.lower() == "no": 
                quit()
            
    else:
        username_again = input("Username incorrect. Would you like to try again? Yes or no?")
        if username_again.lower() == "yes":
            login = True
        if username_again.lower() == "no":
            print("Thank you for trying, welcome back later!")
            quit()                                                                                                                      

