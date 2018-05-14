# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.41(pre-alpha-crapware)

import json
from random import SystemRandom as SR



# Global sigils
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

P0 = (2**256)+1

fart = SR().getrandbits
# Global rituals
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
# Given an integer and a long "prime" find a valid mmi of at least integer size
def findmmi ( mmi_sz, prime, sanity=257 ) :
    if type(mmi_sz) not in [int] : return "I need an int, and a long."
    if type(prime) not in [int, long] : return "I need an int, and a long."
    if prime.bit_length() < mmi_sz : return "Not gonna do it."
    v = (sanity >> 1) + 1
    # our targets
    x = [ (i*prime)+1 for i in range(1,v) ]
    # our sacrifices
    y = fart(mmi_sz)
    print y
    while 1 :
        if sanity == 0 : return "Devoured by shoggoths."
        z = [i % y for i in x ]
        if 0 in z :
            w = x[z.index(0)] / y
            #is it really an mmi of prime?
            if (y * w) % prime == 1 : return (y,w,prime)
        y += 1
        sanity -= 1
    return (x,y,prime)
#
