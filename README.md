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
foo.enchant_hammer(foo.load_secrets('filename'))
```

To import an existing public key,

```
bar = foo.load_publics('filename')
if type(bar) in [str] : print 'some error' + bar
bar = foo.enchant_hammer(bar)

# Or without the check, as a one-liner
foo.enchant_hammer(foo.load_publics('filename'))
```

To encrypt a message,

To decrypt a ciphertext message,

To import a ciphertext,

To export a key, or ciphertext file,

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
