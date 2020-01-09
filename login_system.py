import quiz

users = [
    {
        "username": "ICYLGR01",
        "password": "Cocoban123", 
    },
    {
        "username": "skalman",
        "password": "fruktsallad"
    }
]

# def register(username,password):
#     username = input("Username:")
#     password = input("Password:")
#     return # de nya keyvalue paren läggs in i users

def login(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return True   
    return False

    # return username == users[0+1] password == users[0+1+1]
    # return username == "ICYLGR01" and password == "Cocoban123"   # det ska läggas in från dictionaryn och sedan kunna användas
    # om username är ICYLGR01 och lösenordet är Cocoban123 returnera True, annars returnera False

def register(username,password):
    username = input("Write an username:")
    password = input("Write a password:")
    user_dictionary = {"username": username, "password": password}
    return users.append(user_dictionary)

login_in = True
while login_in:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if login(username, password):
         print("Welcome", username, ", You may now progress to the quiz \n") # du lyckades
         quiz.start()  
         # quizet startas
    else:
        tryagain_register = input("Incorrect, you want to try again? Yes or no?")
        if tryagain_register == "yes".lower():
            login_in = True
         # startas om
        
        if tryagain_register == "no".lower():
            register(username,password)
            quiz.start() 
        # användarnamn och lösenord registreras
