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
# Checks if a password is in the common password list of 25 passwords
def commonPassword(password):
    with open("compass.txt", "r") as file:
        common_passwords = file.read().splitlines()
    if password in common_passwords:
       return True
    else:
        return False
# Scores the password based on strength
def score(password):
    strength = check_strength(password)
    if strength == 4:
        print("Password is strong")
    elif strength == 3:
        print("Password is moderate")
    else:
        print("Password is weak")
#if it is a common password it should not be accepted
def cancel_out(password):
    if commonPassword(password) == True:
        print("Password is commonly used. Please choose a different password.")
    else: 
        check_strength(password)

      
def main():
    password = input("Enter your password: ")
    cancel_out(password)
      
if __name__ == "__main__":
    main()
 