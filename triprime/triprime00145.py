# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)

import forge    # Key/nonce generation
import anvil    # Simple file I/O (json)
import hammer   # Enc./Dec. modes


# Global sigils
VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

DERP = [ "Invalid mode.", "Failed to generate key primitives.",
          ]

# Global rituals
#
#
class TriPrime ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        # Assign known P0 and setup attributes
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0 - 2).bit_length()
        #
    #
    #
    def test0 ( self, mode=512 ) :
        #
        a = forge.HellForge(mode)
        a.gennonces()
        b = a.genkeyparts()
        if b in [1,2,3] : return DERP[1]
        b = a.forgekeypair()
        if b in a.DERP : return b
        b = hammer.BaleHammer(mode)
        b.P1, b.P2 = a.P1, a.P2
        b.P0mmi, b.P1mmi, b.P2mmi = a.P0mmi, a.P1mmi, a.P2mmi
        b.nonces, b.private, b.public = a.nonces, a.private, a.public
        return b


#
if __name__ == '__main__' :
    #
    a = TriPrime().test0(128)
