
# Username = input("Enter the username: ")
# Password = input("Enter the password: ")
# Email = input("Enter the Email-Id: ")

# def website_login(username, password, email):
#     valid = True

#     if len(username) <= 3:
#         print("Username must contain more than 3 characters.")
#         valid = False

#     digit_found = False
#     for ch in password:
#         if ch in '0123456789':
#             digit_found = True

#     if len(password) < 8:
#         print("Password must contain at least 8 characters.")
#         valid = False

#     if digit_found == False:
#         print("Password must contain at least one number.")
#         valid = False

#     if '@' not in email:
#         print("Email must contain @ symbol.")
#         valid = False

#     if valid == True:
#         print("Login Succesful!! Your entered data is correct.")
#     else:
#         print("Please re-try with valid details.")

# website_login(Username, Password, Email)


Username = input("Enter the username")
Password = input("Enter the Password")
Email = input("Enter tha Email-Id")

def web_login(username, password, email):
    vaild = True

    if len(Username) <= 3:
        print("Username must contains 3 character.")
        vaild = False

    digit = False
    for ch in Password:
        if ch in '0123456789':
            digit = True

    if len(Password) < 8 or digit == False:
        print("Password must be 8 characters and atleast one number.")
        vaild = False

    if '@' not in Email:
        print("Email must conatin @ special character.")
        vaild = False

    if vaild == True:
        print("Login Succesful.")
    else:
        print("Login Failed try again")

web_login(Username, Password, Email)