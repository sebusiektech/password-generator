import string
import secrets

def generate_passwd(length=12):

    letters = string.ascii_letters
    
    numbers = string.digits
    
    symbols = string.punctuation

    all_signs = letters + numbers + symbols

    password = ''.join(secrets.choice(all_signs) for i in range(length))

    return password

print("Your new secure password: ", generate_passwd())