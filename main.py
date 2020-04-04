from RSA import *

message = "Lucas is cool!"

rsa = RSA()

print(rsa.check_encryption())

encrypted = rsa.encrypt(message)
decrypted = rsa.decrypt(encrypted)

print(decrypted)
