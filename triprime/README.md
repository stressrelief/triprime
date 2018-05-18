# Code Usage

# Anvil

Importing file like objects (json) is possible with the `anvil` module, which accepts an optional data size (default: 32 bits):

`bar = anvil.BrimstoneAnvil(512)`

The `import_secrets` method will look for a specified file name prefix, in the `/triprime/private/` directory, loading any matching `.secret` key into the `private` dictionary of the instance.

`i = bar.import_secrets('foo')`

*This would attempt to load the file located at `/triprime/private/foo.secret` into `bar.private`.*

The `export_public_key` method will export a specified key, to the `/triprime/public/` directory given a file name prefix. This key is softly checked for validity before export. The method returns the file path for the exported key.

`p = bar.export_public_key(bar.public[0], 'bar')`

The `export_private_key` method will export a specified key, to the `/triprime/private/` directory given a file name prefix. This key is softly checked for validity before export. The method returns the file path for the exported key.

`p = bar.export_private_key(bar.private[0], 'bar')`

The `export_ciphertext` method will export ciphertext, (or any long) to the `/triprime/outgoing/` directory given a file name prefix. The ciphertext is softly checked for validity before export. The method returns the file path for the exported ciphertext.

`p = bar.export_ciphertext(bar.cipher[0], 'bar')`

# Forge

Key generation can be accomplished by the `forge` module, which accepts an optional data size (default: 32 bit):

```
bar = forge.HellForge()
bar = forge.HellForge(512)
```

The `HellForge` class contains methods for generating appropriate nonces, and checking their validity:

```
bar.gen_nonces()
if bar.check_nonces() in [False] : return "Nonce generation failed."
```

The `gen_key_parts` and `check_key_parts` methods are used in a similar fashion:

```
x = bar.gen_key_parts()
if x in [1,2,3] : return "Failed to generate key primitives."
x = bar.check_key_parts()
if x in [False] : return "Key primitive check failed."
```

The `forge_keypair` method will use the calculated key primitives, to create a private/public keypair.

`bar.forge_keypair()`

At this point, the keypair can be imported into the appropriate module below, for further use. (Which is probably not as secure as it should be.)

# Hammer

Encryption, decryption, and data handling is performed by the `hammer` module, which accepts an optional data size (default: 32 bit):

`foo = hammer.BaleHammer(512)`

The `BaleHammer` class contains methods for checking, and applying usable nonces to a particular data segment, depending on data size of the instance:

```
x = foo.check_nonces()
if x in [False] : return "No valid nonce available."
data = foo.use_nonce(data)
```

The `encrypt` method will use a supplied public key, to encrypt supplied data (long type). It will return the index value for the encrypted ciphertext, in the `cipher` dictionary:

```
x = foo.encrypt(foo.public[0], data)
print foo.cipher[x]
```

The `decrypt` method will use a supplied private key, to decrypt supplied ciphertext (long type). It will return the index value for the decrypted data, in the `data` dictionary.
