import re

def is_valid_password(password):
    # Check length
    if len(password) > 12 and len(password) < 6:
        return False
    
    # Check for uppercase and lowercase characters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False
    
    # Check for digits
    if not re.search("[0-9]", password):
        return False
    
    # Check for special characters
    if not re.search("[@#$]", password):
        return False
    
    return True

# Test the function
#password = input("Enter a password: ")
password = "asqwr1234@1,aF145#,2w3E*,2We3345"
pwd_lst = password.split(",")
for pwd in pwd_lst:
    if is_valid_password(pwd):
        print(pwd)
    else:
        print("Password is invalid.")

