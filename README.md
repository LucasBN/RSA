## How to use:

First, you must initialise an encryption class, which takes an optional argument prime_length = 1024 (default):

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

## Sources

1. [Miller-Rabin](https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb)
2. [Cracking RSA](https://www.youtube.com/watch?v=lElHzac8DDI&list=WL&index=10&t=4s)
3. [Improved Wiener Attack](http://einspem.upm.edu.my/journal/fullpaper/vol11saugust/45-57.pdf)
4. [Wiener Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack)
5. [Continued Fractions](https://en.wikipedia.org/wiki/Continued_fraction)

## Future

* Digital signatures
* Cracking RSA
* Add padding + improved parameter selection + salting?
* Fix any potential exploits in the key generation, using crack.py
