# Triprime 
version 0.0.1.45(pre-alpha-crapware)

# Excursions in cryptography for the sake of secrecy, and deniability.
...that's what we tell ourselves.

# Code Usage
Create a new instance of the `TriPrime` class, optionally specifying the data size (default: 32 bit):

```foo = TriPrime()
foo = TriPrime(512)
```

Key generation can be accomplished by the `forge` module, which accepts an optional data size (default: 32 bit):

```bar = forge.HellForge()
bar = forge.HellForge(512)
```

The `HellForge` class contains methods for generating appropriate nonces, and checking their validity:

```bar.gen_nonces()
if bar.check_nonces() in [False] : return "Nonce generation failed."
```

The `gen_key_parts` and `check_key_parts` methods are used in a similar fashion:

```if bar.gen_key_parts() in [1,2,3] : 
    return "Failed to generate key primitives."
if bar.check_key_parts() in [False] : 
    return "Key primitive check failed."
```

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
