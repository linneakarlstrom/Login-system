import csv
import os
userName = input("Enter User Name: ")
passWord = input("Password: ")

fields = ['username','password']

filename = 'data.csv'

# Open file in append mode
with open(filename, 'a', newline='\n') as csvUser:

      # dict is now a dictionary, as required by writerow.
      dict = {'username': userName,'password': passWord}

      writer = csv.DictWriter(csvUser, fieldnames=fields)

      # if it's an empty file, write the header
      if os.stat(filename).st_size == 0:
          writer.writeheader()

      writer.writerow(dict)

csvUser.close()