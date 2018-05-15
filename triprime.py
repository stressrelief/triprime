# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.42(pre-alpha-crapware)

from random import SystemRandom as SR

# Global sigils
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

VALID_MODES = [32,64,128,256,512]

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

fart = SR().getrandbits

# Global rituals
#
def findmmilazy ( rand_sz ) :
    if type(rand_sz) in [int, long] :
        #
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
    return fart(666)
#
# Given an integer and a long "prime" find a valid mmi of at least integer size
def findmmi ( mmi_sz, prime, sanity=256 ) :
    if type(mmi_sz) not in [int] : return "I need an int, and a long."
    if type(prime) not in [int, long] : return "I need an int, and a long."
    if prime.bit_length() < mmi_sz : return "Not gonna do it."
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
# Given the subordinate prime, find a prime that can encapsulate it
def findpee ( gimp, sanity=64 ) :
    if type(gimp) not in [int, long] : return "Unsupported input."
    if 0 in [gimp%i for i in P64] : return "Not a prime."
    # Our pfloor is the max data value the gimp can support
    pfloor = (gimp - 1)**2 # Let it flow...
    w = SR().getrandbits(gimp.bit_length() >> 2)
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
def extendmmi ( x, y, prime ) :
    #
    if (x * y) % prime != 1 : return "Invalid input."
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
            #
        #
    #
    return ret
#

#
class Triprime ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return "Invalid mode."
        #
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0-1).bit_length()
        self.public, self.private, self.cipher = {}, {}, {}
        #
        #
    #
    def forgekeypair ( self ) :
        if len(self.P0mmi) <= 0 : return "No P0mmi found."
        if len(self.P1mmi) <= 0 : return "No P1mmi found."
        if len(self.P2mmi) <= 0 : return "No P2mmi found."
        #
        self.private[len(self.private)] = (
            self.P2mmi[0], self.P2, self.P1mmi[0], self.P1, self.P0mmi[0])
        self.public[len(self.public)] = (
            self.P2mmi[1] * self.P1mmi[1] * self.P0mmi[1], self.P2)
        #
        return None
    #

    #
    def genkeyparts ( self, mode=0, sanity=32) :
        if mode in [0] :
            # Generate P1, and P1 mmi pair
            x = findpee(self.P0)
            c = sanity
            while 1 :
                if c <= 0 : return 1
                y = findmmilazy((x.bit_length()/2)+4)
                if y[2].bit_length() > x.bit_length() :
                    self.P1 = y[2]
                    self.P1mmi = (y[0], y[1])
                    break
                c -= 1
            # Generate P2, and P2 mmi pair
            x = findpee(self.P1)
            c = sanity
            while 1 :
                if c <= 0 : return 2
                y = findmmilazy((x.bit_length()/2)+4)
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
                x = findmmi(24, self.P0, 512)
                if x != 0 :
                    self.P0mmi = (x[0],x[1])
                    break
                sanity -= 1
                #
            return None
            #
        #
    #
    def encrypt ( self, pubkey, data=None ) :
        #
        if data != None :
            #
            x, y = pubkey[0], pubkey[1]
            self.cipher[len(self.cipher)] = (data * x) % y
            return None
            #
        #
    #
    def decrypt ( self, seckey, data=None ) :
        #
        if data != None :
            #
            x = (data * seckey[0]) % seckey[1]
            x = (x * seckey[2]) % seckey[3]
            return (x * seckey[4]) % self.P0
            #
        #
    #
#
if __name__ == '__main__' :
    A = Triprime(512)
    A.genkeyparts()
    A.forgekeypair()
    
