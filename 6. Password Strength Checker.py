import getpass
import re

title = "Password Strength Checker"
character = "*" * len(title)
print(character)
print(title)
print(character)
    

def check_number(password:str) -> bool:
    return bool(re.search(r'[0-9]', password))

def check_uppercase(password:str) -> bool:
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password:str) -> bool:
    return bool(re.search(r'[a-z]', password))

def check_special_characters(password:str) ->bool:
    return bool(re.search(r'[!@#$%&?]', password))

def check_white_spaces(password:str) -> bool:
    return bool(re.search(r'\s', password))

def check_length(password:str) -> bool:
    return 6 <= len(password) <= 12
    
password = getpass.getpass(prompt="Enter your password: ")    

    
while not check_number(password):
    print("Password must have at least one digit (0-9)")
    password = getpass.getpass(prompt="Enter your password: ")
    
while not check_uppercase(password):
    print("Password must have at least one capitalized letter (A-Z)")
    password = getpass.getpass(prompt="Enter your password: ")

while not check_lowercase(password):
    print("Password must have at least one lower letter (a-z)")
    password = getpass.getpass(prompt="Enter your password: ")

while not check_special_characters(password):
    print("Password must have at least one of the following special characters (!#$%&?@))")
    password = getpass.getpass(prompt="Enter your password: ")

while check_white_spaces(password):
        print("Password must not contain any white spaces!")
        password = getpass.getpass(prompt="Enter your password: ")
        
while not check_length(password):
        print("Password length must be at least 6 character and at most 12 characters")
        password = getpass.getpass(prompt="Enter your password: ")

if all([check_number(password),
        check_uppercase(password),
        check_lowercase(password),
        check_special_characters(password),
        not check_white_spaces(password),
        check_length(password)]):
    print("Strong password!!")
else:
    print("Your password is not strong enough.")


#-------------------------------------

check_number(password)
check_uppercase(password)
check_lowercase(password)
check_special_characters(password)
check_white_spaces(password)
check_length(password)

