import secrets
import string
import re


commonPasswords = ["password", "123456", "password123", "admin", "letmein", "qwerty"]


def generatePassword(length, upper, digits, special):
    # build the character pool
    chars = string.ascii_lowercase
    if upper:
        chars = chars + string.ascii_uppercase
    if digits:
        chars = chars + string.digits
    if special:
        chars = chars + string.punctuation

    result = []

    # make sure at least one of each selected type is included
    result.append(secrets.choice(string.ascii_lowercase))
    if upper:
        result.append(secrets.choice(string.ascii_uppercase))
    if digits:
        result.append(secrets.choice(string.digits))
    if special:
        result.append(secrets.choice(string.punctuation))

    # fill the rest
    remaining = length - len(result)
    for i in range(remaining):
        result.append(secrets.choice(chars))

    secrets.SystemRandom().shuffle(result)
    pw = ''.join(result)
    return pw


def checkPasswordSecurity(pw):
    print("\n--- Security Check ---")
    print("  Length        :", len(pw), "characters")

    if re.search(r'[a-z]', pw):
        print("  Lowercase     : yes")
    else:
        print("  Lowercase     : no")

    if re.search(r'[A-Z]', pw):
        print("  Uppercase     : yes")
    else:
        print("  Uppercase     : no")

    if re.search(r'[0-9]', pw):
        print("  Numbers       : yes")
    else:
        print("  Numbers       : no")

    if re.search(r'[^a-zA-Z0-9]', pw):
        print("  Special chars : yes")
    else:
        print("  Special chars : no")

    # score it
    score = 0
    if len(pw) >= 12: score += 1
    if re.search(r'[a-z]', pw): score += 1
    if re.search(r'[A-Z]', pw): score += 1
    if re.search(r'[0-9]', pw): score += 1
    if re.search(r'[^a-zA-Z0-9]', pw): score += 1

    if score == 5:
        print("\n  Verdict: Strong")
    elif score >= 3:
        print("\n  Verdict: Moderate - try increasing length or adding more character types")
    else:
        print("\n  Verdict: Weak")


def askUser(question):
    while True:
        ans = input(question + " (y/n): ").strip().lower()
        if ans == "y":
            return True
        if ans == "n":
            return False
        print("please enter y or n")



print("==================================")
print("       Password Generator")
print("==================================")

# get length from user
while True:
    try:
        length = int(input("\nHow long should the password be? (min 8): "))
        if length < 8:
            print("minimum is 8")
            continue
        break
    except ValueError:
        print("please enter a number")

upper   = askUser("Include uppercase letters?")
digits  = askUser("Include numbers?")
special = askUser("Include special characters?")

pw = generatePassword(length, upper, digits, special)

print("\nGenerated Password:", pw)

checkPasswordSecurity(pw)
