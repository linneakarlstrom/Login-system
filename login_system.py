import quiz
import csv
# import sys
# Programmet ska ej läsa in från listan utan från csv-filen
#  users = [
#     {
#         "username": "ICYLGR01",
#         "password": "Cocoban123", 
#     },
#     {
#         "username": "skalman",
#         "password": "fruktsallad"
#     }
# ]

# def register(username,password):
#     username = input("Username:")
#     password = input("Password:")
#     return # de nya keyvalue paren läggs in i users)

    # return username == users[0+1] password == users[0+1+1]
    # return username == "ICYLGR01" and password == "Cocoban123"   # det ska läggas in från dictionaryn och sedan kunna användas
    # om username är ICYLGR01 och lösenordet är Cocoban123 returnera True, annars returnera False

def create_user():
    new_username = input("Choose your username: \n ")
    new_password = input("Choose your password: \n")
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Username', ' Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({fieldnames[0]: new_username, fieldnames[1]: new_password})


def login():
    username = input("Enter your username: \n")
    password = input("Enter your password: \n")
    with open('data.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row['username'] and password == row['password']:
                quiz.start()
            if username != row['username'] or password != row['password']:
                input("Do you want to try again? Or would you like to create a new login?/ Try again, create login")
                create_user()


        
    


    
# login_in = True
# while login_in:
#     username = input("Enter your username: \n")
#     password = input("Enter your password: \n")
#     if register():
#         print("Welcome", username, ", You may now progress to the quiz \n") # du lyckades
#         quiz.start()  
#          # quizet startas
#     else:
#         tryagain = input("Incorrect, you want to try again? Yes or no? \n")
#         if tryagain == "yes".lower():
#             login_in = True
#          # startas om
        
#         if tryagain == "no".lower():
#             not_login = input("Do you want to register and continue to the quiz, only register or none of the above? \n ")
#             if not_login == "Register and continue to the quiz".lower():
#                 create_user(username, password)
#                 quiz.start() 
#             if not_login == "Only register".lower():
#                 create_user(username, password)
#                 break
#             if not_login == "None of the above".lower() or not_login == "no".lower():
#                 print("Goodbye! Hope to see you soon")
#                 break