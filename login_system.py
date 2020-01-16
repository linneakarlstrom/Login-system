import quiz

def login(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return True   
    return False

    # return username == users[0+1] password == users[0+1+1]
    # return username == "ICYLGR01" and password == "Cocoban123"   # det ska läggas in från dictionaryn och sedan kunna användas
    # om username är ICYLGR01 och lösenordet är Cocoban123 returnera True, annars returnera False

def register(username, password):
    thedata = {"username": username, "password": password}
    import csv
    with open('data.csv', 'w+') as file:
        writer = csv.writer(file)    

login_in = True
while login_in:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if login(username, password):
         print("Welcome", username, ", You may now progress to the quiz \n") # du lyckades
         quiz.start()  
         # quizet startas
    else:
        tryagain = input("Incorrect, you want to try again? Yes or no?")
        if tryagain == "yes".lower():
            login_in = True
         # startas om
        
        if tryagain == "no".lower():
            not_login = input("Do you want to register and continue to the quiz, only register or none of the above?")
            if not_login == "Register and continue to the quiz".lower():
                register(username, password)
                quiz.start() 
            if not_login == "Only register".lower():
                register(username, password)
                break
            if not_login == "None of the above".lower():
                print("Goodbye! Hope to see you soon")
                break