# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)

from random import SystemRandom as SR

# Global sigils
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

DERP = [ "Invalid mode.", "findmmi() needs an int, and a long.",
         "Candidate mmi is too large for given prime.", "Unsupported input.",
         "Not a prime.", "No P0 MMI found.", "No P1 MMI found.",
         "No P2 MMI found.",
    ]

#
# Global rituals
#

class HellForge ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.P1, self.P2 = 0, 0
        self.P0mmi, self.P1mmi, self.P2mmi = [], [], []
        self.size = (self.P0-2).bit_length()
        self.nonce_sz = self.size >> 3
        self.nonces = [ long(0) for i in range(self.nonce_sz >> 1) ]
        self.public, self.private = {}, {}
        #
        self.DERP = DERP
        #
    #
    #
    def check_nonces ( self ) :
        #
        x, y, z = len(self.nonces), len(set(self.nonces)), self.nonce_sz >> 1
        if x == y :
            if x == z :
                return True
            #
        return False
    #
    #
    def check_key_parts ( self ) :
        #
        v, w = self.P1.bit_length(), self.P2.bit_length()
        x, y, z = len(self.P0mmi), len(self.P1mmi), len(self.P2mmi)
        self.key_check = { 'P1bit' : v, 'P2bit' : w, 'P0mmi' : x,
                           'P1mmi' : y, 'P2mmi' : z }
        if 0 in [ v, w, x, y, z ] :
            return False
        #
        return True
    #
    #
    def findmmilazy ( self, rand_sz ) :
        fart = SR().getrandbits
        if type(rand_sz) in [int, long] :
            x = fart(rand_sz)
            y = fart(rand_sz)
            p = (x * y) - 1
            # find a damn prime
            while 1 :
                if 0 in [p%i for i in P64] :
                    y += 1
                    p = (x * y) - 1
                elif (x * y) % p == 1 :
                    return [x,y,p]
                #
    #
    #
    def findmmi ( self, mmi_sz, prime, sanity=256 ) :
        if type(mmi_sz) not in [int] : return DERP[1]
        if type(prime) not in [int, long] : return DERP[1]
        if prime.bit_length() < mmi_sz : return DERP[2]
        fart = SR().getrandbits
        v = (sanity >> 1) + 1
        # our targets
        x = [ (i*prime)+1 for i in range(1,v) ]
        # our sacrifices
        y = fart(mmi_sz)
        while 1 :
            if sanity == 0 : return 0 #"Devoured by shoggoths."
            z = [i % y for i in x ]
            if 0 in z :
                w = x[z.index(0)] / y
                #is it really an mmi of prime?
                if (y * w) % prime == 1 : return (y,w,prime)
            y += 1
            sanity -= 1
        return (x,y,prime) # Never
    #
    #
    def findpee ( self, gimp, sanity=64 ) :
        if type(gimp) not in [int, long] : return DERP[3]
        if 0 in [gimp%i for i in P64] : return DERP[4]
        fart = SR().getrandbits
        # Our pfloor is the max data value the gimp can support
        pfloor = (gimp - 1)**2 # Let it flow...
        w = fart(gimp.bit_length() >> 2)
        x = pfloor + w
        if x%2 == 0 : x += 1
        while 1 :
            if sanity == 0 : break
            if 0 not in [x%i for i in P64] :
                return x
            x += 2
            sanity -= 1
            #
        #
        return 0 #"Devoured by shoggoths."
    #
    #
    def extendmmi ( self, x, y, prime ) :
        if (x * y) % prime != 1 : return DERP[3]
        #
        ret = {}
        w = [ y%i for i in P64 ]
        print w
        if 0 in w :
            a = y / P64[w.index(0)]
            b = x * P64[w.index(0)]
            if (a * b) % prime == 1 :
                ret[a] = b
        w = [ x%i for i in P64 ]
        print w
        if 0 in w :
            a = x / P64[w.index(0)]
            b = y * P64[w.index(0)]
            if (a * b) % prime == 1 :
                ret[a] = b
        return ret
    #
    #
    def forge_keypair ( self ) :
        if len(self.P0mmi) <= 0 : return DERP[5]
        if len(self.P1mmi) <= 0 : return DERP[6]
        if len(self.P2mmi) <= 0 : return DERP[7]
        #
        self.private[len(self.private)] = (
            self.P2mmi[0], self.P2, self.P1mmi[0], self.P1, self.P0mmi[0])
        self.public[len(self.public)] = (
            self.P2mmi[1] * self.P1mmi[1] * self.P0mmi[1], self.P2)
        #
        return None
    #
    #
    def gen_key_parts ( self, mode=0, sanity=32) :
        if mode in [0] :
            # Generate P1, and P1 mmi pair
            x = self.findpee(self.P0)
            c = sanity
            while 1 :
                if c <= 0 : return 1
                y = self.findmmilazy((x.bit_length()/2)+4)
                if y[2].bit_length() > x.bit_length() :
                    self.P1 = y[2]
                    self.P1mmi = (y[0], y[1])
                    break
                c -= 1
            # Generate P2, and P2 mmi pair
            x = self.findpee(self.P1)
            c = sanity
            while 1 :
                if c <= 0 : return 2
                y = self.findmmilazy((x.bit_length()/2)+4)
                if y[2].bit_length() > x.bit_length() :
                    self.P2 = y[2]
                    self.P2mmi = (y[0], y[1])
                    break
                c-= 1
                #
            # BS to increase our chances of finding one
            sanity = 1024
            #
            while 1 :
                if sanity <= 0 : return 3
                x = self.findmmi(24, self.P0, 512)
                if x != 0 :
                    self.P0mmi = (x[0],x[1])
                    break
                sanity -= 1
                #
            return None
            #
        #
    #
    def gen_nonces ( self ) : # more fun to say
        fart = SR().getrandbits
        x = [ fart(self.nonce_sz) for i in self.nonces ]
        if len(set(x)) == len(x) :
            self.nonces = x
            #
        #
        else : self.gen_nonces()
