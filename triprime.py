# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)

import triprime.forge as forge    # Key/nonce generation
import triprime.anvil as anvil    # Simple file I/O (json)
import triprime.hammer as hammer   # Enc./Dec. modes

# Global sigils
VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

DERP = [ "Invalid mode.", "Nonce generation failed.",
         "Failed to generate key primitives.",
          ]

# Global rituals
#
#
class TriPrime ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        # Assign known P0 and setup attributes
        self.mode = mode
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0 - 2).bit_length()
        #
    #
    #
    def test0 ( self, ) :
        #
        mode = self.mode
        a = forge.HellForge(mode)
        a.gen_nonces()
        b = a.check_nonces()
        if b in [False] : return DERP[1]
        b = a.gen_key_parts()
        if b in [1,2,3] : return DERP[2]
        b = a.check_key_parts()
        if b in [False] : return DERP[2]
        # perform experimental mmi extension
        #b = a.extend_key()
        #if b in [False] : return " "
        b = a.forge_keypair()
        if b in a.DERP : return b
        b = hammer.BaleHammer(mode)
        b.private, b.public, b.nonces = a.private, a.public, a.nonces
        # Hammer enchanted!
        return b
    #
    #
    def test1 ( self, ) :
        #
        a = anvil.BrimstoneAnvil(self.mode)
        b = self.test0()
        #


#
if __name__ == '__main__' :
    #
    a = TriPrime(128).test0()
