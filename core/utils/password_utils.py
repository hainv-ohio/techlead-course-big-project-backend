import bcrypt

def get_hashed_password(plain_text_password, salt):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, salt)