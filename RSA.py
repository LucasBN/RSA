class RSA:

    def __init__(self):
        self.p = 7817
        self.q = 7741
        self.e = 65537
        self.generate_keys()

    def get_public_key(self):
        return self.public_key

    def string_to_ascii(self, message):
        return [ord(c) for c in message]

    def ascii_to_string(self, c):
        return chr(c)

    def mod_power(self, power, base, mod):
        if power == 1:
            return base % mod
        elif (power % 2) == 0:
            return ( (self.mod_power(power/2, base, mod) ** 2) % mod )
        else:
            return ( (self.mod_power(1, base, mod) * self.mod_power(power-1, base, mod)) % mod )

    def phi_primes(self):
        return ((self.p-1) * (self.q-1))

    def hcf(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.hcf(b % a, a)
            return (g, x - (b // a) * y, y)

    def modular_inverse(self):
        g, x, y = self.hcf(self.e, self.phi_pq)
        return x % self.phi_pq

    def generate_keys(self):
        self.pq = self.p*self.q
        self.phi_pq = self.phi_primes()
        self.public_key = [self.pq, self.e]
        self.private_key = self.modular_inverse()
        return [self.public_key, self.private_key]

    def encrypt(self, message):
        return [self.mod_power(self.public_key[1], c, self.public_key[0]) for c in self.string_to_ascii(message)]

    def decrypt(self, ciphertext):
        return ''.join([self.ascii_to_string(self.mod_power(self.private_key, c, self.public_key[0])) for c in ciphertext])
