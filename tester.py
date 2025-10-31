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
    lostrings = []
    if len(password) >= 8:
        strength += 1
    else:
       lostrings.append("Password length should be 8 or more characters.\n")
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    else:
        lostrings.append("Password should contain both uppercase and lowercase letters.\n")
    if re.search("[0-9]", password):
        strength += 1
    else:
        lostrings.append("Password should contain at least one digit.\n")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        lostrings.append("Password should contain atleast one special character.\n")
    
    return  strength, lostrings

# Scores the password based on strength
def score(password):
    strength,lostrings = check_strength(password)
    
    if strength == 4:
        msg = ("Password is strong.\n")
    elif strength == 3:
        msg=("Password is moderate.\n")
    else:
        msg = ("Password is weak.\n")
    if lostrings:
        msg += "Recommendations:\n\n" + "".join(lostrings)
    return msg


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
       
# #Grabs password from user 
# def main():
#     password = input("Enter your password: ")
#     if pwned_check(password) > 0:
#         count = pwned_check(password)
#         print(f"Password has been compromised {count} times! Please choose a different password.")
#     else:
#         score(password)
#         print("Password has not been found in any data breaches.")
    
    
# #calls main function
# if __name__ == "__main__":
#     main()
 