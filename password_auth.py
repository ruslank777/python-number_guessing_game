import getpass

db = {"omen.abrek": "123456", "john.doe": "654321"}
username = input("Please enter username: ")
# getpass method will hide the input values
password = getpass.getpass("Please enter password: ")

# Let's iterate via the db to find the username - password combination by the username that was entered
for i in db.keys():
    if username == i:
        # While loop to give user several attempts to enter a password if the first attempt was wrong
        while password != db.get(i):
            password = getpass.getpass("Please enter your password again: ")
        break
print("Login successful")
