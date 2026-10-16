
Username = input("Enter the username: ")
Password = input("Enter the password: ")
Email = input("Enter the Email-Id: ")

def website_login(username, password, email):
    valid = True

    if len(username) <= 3:
        print("Username must contain more than 3 characters.")
        valid = False

    digit_found = False
    for ch in password:
        if ch in '0123456789':
            digit_found = True

    if len(password) < 8 or digit_found == False:
        print("Password must contain at least 8 characters and atleast 1 digit.")
        valid = False

    if '@' not in email:
        print("Email must contain @ special symbol.")
        valid = False

    if valid == True:
        print("Login Succesful!! Your entered data is correct.")
    else:
        print("Please re-try with valid details.")

website_login(Username, Password, Email)


