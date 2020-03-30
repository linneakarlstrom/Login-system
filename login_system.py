import quiz
import csv


def create_user():
    print("CREATE YOUR ACCOUNT")
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
        for row in reader:
            if username == row['Username'] and password == row['Password']:
                return True
            else:
                return False

def login():
    print("LOGIN WITH YOUR USERNAME AND PASSWORD")
    username = input("Enter your username: \n")
    password = input("Enter your password: \n")
    if user_exists(username, password):
        quiz.start()
    else:
        create_user()

login()