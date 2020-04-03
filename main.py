from RSA import *

message = "Lucas is cool!"

rsa = RSA()

encrypted = rsa.encrypt(message)
decrypted = rsa.decrypt(encrypted)

print(decrypted)
