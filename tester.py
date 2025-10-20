import re
import hashlib
import requests

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
        print ("Password length should be 8 or more characters")
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
        print("Password is strong.")
    elif strength == 3:
        print("Password is moderate.")
    else:
        print("Password is weak.")
#if it is a common password it should not be accepted
def cancel_out(password):
    if commonPassword(password) == True:
        print("Password is commonly used. Please choose a different password.")
    else: 
        score(password)

# Incorpatee getPawned API to check if password has been compromised
def pwned_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5_char}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.")
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0
       
#Grabs password from user 
def main():
    choice = input("Enter 1 to check password strength or 2 to check if password has been compromised: ")
    password = input("Enter your password: ")
    if choice == '1':
        cancel_out(password)
    elif choice == '2':
        count = pwned_check(password)
        if count:
            print(f"Password has been compromised {count} times! Please choose a different password.")
        else:
            print("Password has not been found in any data breaches.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
#calls main function
if __name__ == "__main__":
    main()
 