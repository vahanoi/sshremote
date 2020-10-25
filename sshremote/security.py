"""Password storrage module
scrypt/bcrypt main password to decrypt password file
"""
import scrypt
import hashlib
import os
import getpass

# TODO test
def encode_password (password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password = getpass.getpass(prompt="Password: ")
    spass = scrypt.encrypt(salt, password,maxtime=0.5)



def decode_password(password)
    test = scrypt.decrypt(spass,password,maxtime=0.5)
    print (test)
