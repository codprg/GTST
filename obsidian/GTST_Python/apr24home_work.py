# Given list of users with username,password sequence
users = [
    "Nathan,'231Geeg'",
    "Geese,'pass231Abhee'",
    "092131313,'Milk','P!34$OnD'[H4ck3M']"
]

# Separate usernames and passwords
usernames = []
passwords = []

for user in users:
    parts = user.split(",'")
    usernames.append(parts[0])
    passwords.append(parts[1])

# Sort usernames and passwords
usernames.sort()
passwords.sort()

# Display the sorted lists
print("The usernames are:", ", ".join(usernames))
print("Passwords are:", ", ".join(passwords))


# Create a dictionary mapping usernames to passwords
user_password_dict = {}
for user in users:
    parts = user.split(",'")
    user_password_dict[parts[0]] = parts[1]

# Get input from the user
input_username = input("Enter your username: ")

# Find the corresponding password
if input_username in user_password_dict:
    print(f"Your password is: {user_password_dict[input_username]}")
else:
    print("Username not found.")
