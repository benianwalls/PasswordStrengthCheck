import re
# Strength rules

# Password length > 8
# Letter case - contains both uppercase and lowercase letters
# Numbers - contains atleast one digit
# Special characters - contains atleast one special character
# Common Passwrod check = not in common password list


def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    else:
        print ("Password length should be greater than 8")
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    else:
        print ("Password should contain both uppercase and lowercase letters")
    if re.search("[0-9]", password):
        strength += 1
    else:
        print ("Password should contain atleast one digit")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print ("Password should contain atleast one special character")
    return strength
def commonPassword(password):
    with open("compass.txt", "r") as file:
        common_passwords = file.read().splitlines()
    if password in common_passwords:
       print("Password is commonly used. Please choose a different password.")
    else:
        print("Password is not in the common password list.")
def main():
    password = input("Enter your password: ")
    check_strength(password)
    commonPassword(password)   
if __name__ == "__main__":
    main()
 