# Define the user information dictionary
users = {
    'Nathan': 'pass231',
    'Geez': 'pass231',
    'Abebe': '092313133',
    'Miki': "pl3s34D0n'tH4ckM3"
}

# Initialize login attempts counter
login_attempts = 0

# Loop for up to 5 login attempts
while login_attempts < 5:
    # Accept username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists in the dictionary and if the password matches
    if username in users and users[username] == password:
        print("Welcome to GTST Company!")
        break  # Exit the loop if login is successful
    else:
        print("Incorrect Login! Please try again.")
        login_attempts += 1

# If login failed 5 times, display the "Sorry, you are limited!" message
if login_attempts == 5:
    print("Sorry, you are limited!")
