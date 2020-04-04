## How to use:

First, you must initialise an encryption class:

```
from RSA import *

rsa = RSA()
```

To encrypt a message:

```
message = "Lucas is cool!"
encrypted = rsa.encrypt(message)
```

To decrypt a message:

```
decrypted = rsa.decrypt(encrypted)
```

To get the public_key:

```
rsa.get_public_key()
```

To ensure that the prime generation was successful:

```
print(rsa.check_encryption())
```

## Prime Generation Method

To generate primes p and q, the Miller-Rabin primality test is used. Sometimes, the Miller-Rabin test says that a composite number is prime, although the chance of this is very low. Bits of length 1024 are repeatedly randomly generated and primality tested. When a prime is found, it is returned. To check that the primes are actually prime, the function ```check_encryption()``` which takes no arguments, returns a True value if the encryption and decryption was successful on a test string. If the function returns false, the primes must be regenerated. Any random bits used to generate the primes are subsequently removed from memory.
