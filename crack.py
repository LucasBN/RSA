from RSA import *

#### Attempt to crack the RSA algorithm:

### Prime number selection weaknesses:

## Reusing prime numbers, GCD can be found (one of the primes used)
## If p and q share half their upper bits, pq can be factored using Fermat's method
## If p or q contain too many contiguous zeros, Coppersmith's method can be used to factor pq
## If (p - 1) or (q - 1) has a small prime factor, Pollard (p-1) can be used to factor pq

### Private key exponent weaknesses:

## Small d speeds up decryption but if d < (pq)^0.25, private key can be recovered using continued fractions (Chinese RT can be used to work around this)

### Public key exponent:

## {2, 3, 17, 65537} - Fermat Prime

rsa = RSA(256)
if not rsa.check_encryption():
    quit()
pub_key = rsa.get_public_key()

## Test if small enough private key:

d_len = len('4674517606962530021492709117550967227657429450402249506333528278879163047714847921140086115671957347574981652444426214041214442931949268943256629677053473')

if (d_len**2)*pub_key[1] < 8 * pow(pub_key[0], 1.5):
    print("Vulnerable to small private key attack")
