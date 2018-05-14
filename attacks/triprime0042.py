# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.42(pre-alpha-crapware)

import json
from random import SystemRandom as SR



# Global sigils
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

VALID_MODES = [4,8,16,32,64,128,256,512]

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

fart = SR().getrandbits
# Global rituals
#
def findmmilazy ( rand_sz ) :
    #fart = SR().getrandbits
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
    #print y
    while 1 :
        if sanity == 0 : return "Devoured by shoggoths."
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
    w = SR().getrandbits(gimp.bit_length() >> 1)
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
    return "Devoured by shoggoths."
#


#
if __name__ == '__main__' :
    a = findpee(PRIMES[7])
    print a.bit_length()
    b = findmmilazy(a.bit_length())
    print b[2].bit_length()
    c = findpee(b[2])
    print c.bit_length()
    A = [ findmmi(24,a,1024) for i in range(8)]
    #
