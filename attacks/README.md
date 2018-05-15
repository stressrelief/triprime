# Attacking the 4 bit encryption
The most forthcoming solution would be to encrypt the potential data vectors with the given public key, then match the results to the corresponding ciphertext.

The 4 bit limitation of the data is the weakest point of attack. Any attempts at mitigations should look there, first.

# Maybe a bigger data size?
A larger data size would increase the difficulty of this brute force attack. However, we must keep a 1:8 ratio between our data and ciphertext. This means, our P0 value would need to increase to support a larger data size, which would increase the size of P1, and P2. For a 128 bit data size, we would need primes of 128, 256, and 512 bits, with modular multiplicative inverses for key genertaion...

# We found a lazy way...
That makes relatively small private keys... and we found an even lazier way to generate our random values... too lazy?

# What if we just fake it?
We could generate a large random number, multiply it by `self.p0 -1` and be on our way. That way our underlying 4 bit data remains unchanged after decryption, but the difficulty of the prior attack, can easily become 'impossible.' But we just end up losing data, that way... maybe we can keep that for something later...

# Public key woes
Notice how the P2 value in the public key is always (usually) larger than the preceding mmi product. That could be a problem.

If a sufficiently small data value is multiplied by a sufficiently small mmi product, the modular reduction by P2 will be ineffective. Trivial division by the public key's mmi product would reveal the underlying data value.

`foo = Triprime(512)`

`foo.genkeyparts()`

`foo.forgekeypair()`

`foo.encrypt(foo.public[0], 1337)`

`foo.cipher[0] / foo.public[0][0]`

`1337L`


It's for this reason, a better method must be used...
