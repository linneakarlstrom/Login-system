import quiz
import csv


def create_user():
    print("\nCREATE YOUR ACCOUNT")
    new_username = input("Choose your username: ")
    new_password = input("Choose your password: ")
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({fieldnames[0]: new_username, fieldnames[1]: new_password})
    login()

def user_exists(username, password):
    with open('data.csv','r') as file:
        reader = csv.DictReader(file)
        exists = False
        for row in reader:
            if username == row['Username'] and password == row['Password']:
                exists = True
        return exists

def login():
    print("\nLOGIN WITH YOUR USERNAME AND PASSWORD")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_exists(username, password):
        quiz.start()
    else:
        choose = input("Do you want to try again or would you like to create a new user? \n[again / create]\n")
        if choose == "again":
            login()
        if choose == "create":
            create_user()

login()