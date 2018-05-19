# triprime 
version 0.0.1.46(pre-alpha-crapware)

# Excursions in cryptography for the sake of secrecy, and deniability.
...that's what we tell ourselves.

# Code Usage
Create a new instance of the `TriPrime` class, optionally specifying the data size (default: 32 bit):

```
foo = TriPrime()
foo = TriPrime(512)
```

# Key generation, and importation

To create a new keypair, use the `forge_hammer` method. The `public` and `private` dicts will contain the respective keys.

```
bar = foo.forge_hammer()
bar.public[0]
bar.private[0]
```

To import an existing private key, 

```
bar = foo.load_secrets('filename')
if type(bar) in [str] : print 'some error' + bar
bar = foo.enchant_hammer(bar)

# Or without the check, as a one-liner
bar = foo.enchant_hammer(foo.load_secrets('filename'))
```

To import an existing public key,

```
bar = foo.load_publics('filename')
if type(bar) in [str] : print 'some error' + bar
bar = foo.enchant_hammer(bar)

# Or without the check, as a one-liner
bar = foo.enchant_hammer(foo.load_publics('filename'))
```

# Encryption and Decryption

To encrypt a message, the `encrypt` method is used with a proper public key, and some `long` data. It will return the key/index value for where the ciphertext is stored, in the `cipher` dict. (Assuming `bar` is a properly accursed relic.):

```
ckey = bar.encrypt(bar.public[0], some_long_data)
print bar.cipher[ct_key]
```

To decrypt a ciphertext message, the `decrypt` method is used with a proper private key, and some ciphertext. It will return the key/index value for where the decrypted data is stored, in the `data` dict. (Assuming `bar` is a properly accursed relic.):

```
dkey = bar.decrypt(bar.private[0], some_ciphertext)
print bar.data[dkey]
```

To import a ciphertext, the `load_incoming` method is provided. With a valid file name, or list of valid file names, it will attempt to load the specified ciphertext files (in the `incoming` subdirectory) into an instance of `anvil`. The `anvil` instance is returned with the ciphertext files loaded, in order, in the `cipher` dict.

```
bar = foo.load_incoming(['foo', 'bar'])
print bar.cipher[0]
```

To export a key, or ciphertext file, the `export_file` is used. Given valid `filedata`, (such as a public key, ciphertext, etc.) a valid file name, and a valid file type (public, private, cipher etc.) the method will export the file. This method returns a string pointing to the directory location of the file written.

```
fp = foo.export_file(some.public[0], 'ex00', 'public')
print fp

fp1 = foo.export_file(some.private[0], 'ex00', 'private')
fp2 = foo.export_file(some.cipher[0], 'msg0', 'cipher')
```

(**Note**: This will be replaced with a profile system, to avoid key confusion.)

# Nonsense

Consider an object, D, of a fixed bit size.

Now, fathom a prime, P0, large enough (larger than) to encapsulate that object.
Let us assume we have divined the modular multiplicative inverses of P0, P0(i,\`i), and can conjure them at will.

We have all the reagents for a disastrous ritual to summon forth Assymetricyptogorgonomicron.

`Assymetricyptogorgonomicron`

Using the darkest of arts, we will evoke two more primes, the first, P1, large enough to encapsulate D and the size of P0. The second prime, P2, at least twice the size of P1. Mysteriously, we have P1(i,\`i), and P2(i,\`i) modular multiplicative inverses.

/The ancient tome is missing several pages here/

...when aligned, shall conjure a divine key, which can be used with the sign of the Dark S...

/The ancient tome is missing several pages here/
