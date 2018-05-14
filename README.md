# triprime 
0.0.1.4(pre-alpha-crapware)

# Excursions in cryptography for the sake of secrecy, and deniability.
...that's what we tell ourselves.

# Basics
Consider an object, D, of a fixed bit size.

Now, fathom a prime, P0, large enough (larger than) to encapsulate that object.
Let us assume we have divined the modular multiplicative inverses of P0, P0(i,\`i), and can conjure them at will.

We have all the reagents for a disastrous ritual to summon forth Assymetricyptogorgonomicron.

`Assymetricyptogorgonomicron`

Using the darkest of arts, we will evoke two more primes, the first, P1, large enough to encapsulate D and the size of P0. The second prime, P2, at least twice the size of P1. Mysteriously, we have P1(i,\`i), and P2(i,\`i) modular multiplicative inverses.

/The ancient tome is missing several pages here/

# Code Usage
Create a new instance of the triprime class:

`foo = Triprime()`

(Currently, data_sz is forced into a whopping 4-bit data size, for demonstration.)

After creating a new instance, you will need to calculate the MMIs for P2 (See code notes.):

`foo.p2i = findmmi(foo.p2)`

This will take a few minutes, depending on your system specifications. After it completes, you can use the genkeypair() method to create a private, and public, keypair. **Note**: the `output0.json` file contains this data, and can be loaded to save time.

`foo.genkeypair()`

Your keys will be stored in the public, and private, dictionaries, with corresponding key values. You may use the encrypt method with a valid public key, which will request a 4 bit data input, however, it will accept a much larger input:

`foo.encrypt(foo.public[0])`

The underlying ciphertext is stored in the cipher dictionary. You may use the decrypt method, with a valid ciphertext, and private key, in order to recover the data selection from the encrypt method.

`foo.decrypt(foo.cipher[0], foo.private[0])`
