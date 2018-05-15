# triprime 
0.0.1.43(pre-alpha-crapware)

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

`foo = Triprime(256)`

By default, a data size of 32 bits will be used (`mode=32`) however the following modes are now valid:

`[ 32, 64, 128, 256, 512 ]`


The genkeyparts() method is used to create the necessary primes, and some usable modular multiplicative inverses, for those primes. It is used in conjuction with the forgekeypair() method to generate a keypair in the public, and private dictionaries of the instance.

`foo.genkeyparts()`

`foo.forgekeypair()`

Your keys will be stored in the public, and private, dictionaries, with corresponding key values. You may use the encrypt method with a valid public key, and a valid input, no larger than the instance's mode, in bits:

`foo.encrypt(foo.public[0], my_data_int)`

The underlying ciphertext is stored in the cipher dictionary. You may use the decrypt method, with a valid ciphertext, and private key, in order to recover the data selection from the encrypt method.

`foo.decrypt(foo.private[0], foo.cipher[0])`

# File operations
The json library is utilized to easily import, or export key, or ciphertext data. New methods have been implemented in the Triprime class to exploit these features:

`foo.exportkeys('file_name')`

`foo.exportciphertext('file_name')`

An optional index value can be included to specify which item from the appropriate dictionary, should be exported.

`foo.exportkeys('file_name',2)`

The above would export `foo.public[2]` and `foo.private[2]` to `file_name.public.json` and `file_name.secret.json`, respectively. **Note**: Currently only simple file operations are supported; All output will reside within the same directory as triprime.py

`foo.importpubkey('file_name')`

Will import the specified public key (or anything, really) and place it into the next available key in the public dictionary.

`foo.importseckey('file_name')`

"Hey there, sec key..." Imports the selected file into the next available key in the private dictionary.

`foo.importciphertext('file_name')`

Imports the selected file into the next available key in the cipher dictionary.

# Onward...
A new method has been added for determining an mmi pair, for a given prime, when supplied with only 1 random value (half of the mmi pair) and a size in bits, for a random value. These are used to calculate a composite, then test the primality (like a fart on Jupiter) of their product minus one.

`foo.findmmilazy(1234567890,8)`

This will be a component of key creation for accomodating larger data sizes, as we approach something 'better.'

`foo.findmmilazy(SR().getrandbits(2048),2048)`

Other fun methods have also been added...


