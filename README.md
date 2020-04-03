## How to use:

First, you must initialise an encryption class:

```
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

## Features to implement:

* Generate primes according to the [FIPS 186-3](https://csrc.nist.gov/csrc/media/publications/fips/186/3/archive/2009-06-25/documents/fips_186-3.pdf) standards
