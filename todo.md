
#TODO Work file

~~Separate hemorrhaging Triprime into keyforge, and client~~

Proper metaclass impl.

Separate enc/dec functionality from hammer, into 2 independent modules

Separate export/import functionality from anvil

Profile struct and module

CLI interface

Improved file handling

Implement mmiextend functionality for key generation

Implement optional MAC for encrypt method

Implement optional digital signing

Refactor genkeyparts and forgekeypair methods (More accurate sanity for 99.99% success rate)

Begin testing for authenticated encryption

Implement symmetric cipher and hash suites

New key/file format

~~Continue testing on cipher/key encapsulation, and "the 3rd and 4th kinds of keys"~~

Define new protocol design for multi-party key agreement protocol (Default to fortune proto but new is better... right?)

Test bootstrapping, and other homomorphic properties (Simple addition voting via a multi key, and issued "ballots." ZKP proofing between a distributed "Victor" and an anonymous "Peggy". Threshhold encryption tests, with selected key poisoning.)

**Upgrade to Python 3.6 for secrets**

Begin research on embedding the "Ouroboros" (Basically, getting multiple nodes to sync/run the "client" sw, then getting that distributed execution network to load a new distributed node/client.)

Continue research into a unified function, for all nodes, limiting the surface area available for analysis, somewhat. (All nodes would push 3 variables thru the exact same code, generating a valid, encrypted response, or at least, the bulk of it. This small section of code would be over 50-90% of the node runtime code.)
