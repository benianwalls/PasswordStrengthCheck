import re
# Strength rules
'''
Password length > 8
Letter case - contains both uppercase and lowercase letters
Numbers - contains atleast one digit
Special characters - contains atleast one special character
Common Passwrod check = not in common password list

'''
def check_length(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    else:
        print ("password length should be greater than 8")