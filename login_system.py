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
        else:
            return False

    # return username == users[0+1] password == users[0+1+1]
    # return username == "ICYLGR01" and password == "Cocoban123"   # det ska läggas in från dictionaryn och sedan kunna användas
    # om username är ICYLGR01 och lösenordet är Cocoban123 returnera True, annars returnera False

def register():
    return

login_in = True
while login_in:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if login(username, password):
         print("Welcome", username, ", You may now progress to the quiz \n") # du lyckades
         quiz.start()  
         # quizet startas
    else:
        print("Incorrect, you may try again.")
        login_in = True
        # startas om
