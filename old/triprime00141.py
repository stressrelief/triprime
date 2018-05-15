
# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.41(pre-alpha-crapware)

import json
from random import SystemRandom as SR



# Global vars
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

# P32 = (2**256)+1    # 
P16 = (2**16)+1     # 65537
P8 = (2**8)+1       # 257
P4 = (2**4)+1       # 17

# Global funcs
def Ints2Chrs ( in_ls ) :
    return [ chr(i) for i in in_ls ]
#
def Chrs2Str ( in_ls ) :
    ret = ''
    for i in in_ls : ret = ret + i
    return ret
#
def Ints2Str ( in_ls ) :
    ret = Ints2Chrs(in_ls)
    return Chrs2Str(ret)
#
def Str2Ints ( in_ls ) :
    return [ int(i.encode("hex"),16) for i in in_ls ]
#
def findmmilazy ( mmi, rand_sz ) :
    if type(mmi) in [int, long] :
        x = mmi
        print x
    if type(rand_sz) in [int, long] :
        if rand_sz < mmi :
            y = SR().getrandbits(rand_sz)
            print y
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
    return None
#
def findmmi ( prime, x=None ) :
    a = prime - 1
    b = prime + 1
    if x != None :
        c = (b // x) - 1 # c = 2
        if c == 0 :
            c = b // 2
            print c, prime, (prime - c), b.bit_length()
            while (x * c) % prime != 1 :
                c -= 1
                if c < 2 : return "Error0"
            return c
        print c, prime, (prime - c), b.bit_length()
        while (x * c) % prime != 1 :
            c += 1
            if c > prime : return "Error1"
        return c
    #
        
    c,d = [i for i in range(2,b)], [i for i in range(2,b)]
    ret = {}
    if ( a * a ) % prime == 1 :
        ret[a] = a
        # Modified for test2 function testing
        #ret[0] = prime
        #
        c.remove(a)
        d.remove(a)
    else : return "Not prime."
    for i in c :
        for n in d :
            if ( i * n ) % prime == 1 :
                ret[i] = n
                d.remove(n)
                #d.remove(i)
                break
            #
        #
    #
    return ret
    #
#

# D = a fixed data size.
# P0 = a prime larger than D, with a known MMI pair (modular 
# multiplicative inverse: P0(mmi,`mmi)).
# P1 = a prime larger than... D + size(P0), with a known MMI pair.
# P2 = a prime larger than... size(P1 * 2), with a known MMI pair.
# Assume D and P0 are known.
# Public: P0(mmi) * P1(mmi) * P2(mmi), P2
# Private: P2(`mmi), P1(`mmi), P0(`mmi), P1
# Encrypt: data * P0(mmi) * P1(mmi) * P2(mmi) mod P2
# Decrypt: [Exercise left for the reader.]

# class object containing basic methods for generating a proper keypair,
# encrypting some data, and decrypting that data.
class Triprime ( ) :
    def __init__ ( self, data_sz=4 ) :
        if type(data_sz) in [int, long] :
            # 
            x = 2**data_sz
            y = x * x
            z = y * y
            self.pfloor = x,y,z # Ew! Gross!
            self.public, self.private, self.cipher = {}, {}, {}
            # Simple demonstration
            # Overrides functionality... remove.
            self.ds = 4
            self.p0 = P4
            self.p0i = findmmi(self.p0)
            self.p1 = P8 # But it's totally a secret... shh...
            self.p1i = findmmi(self.p1)
            self.p2 = P16
            #self.p2i = findmmi(self.p2)
            with open('output0.json','r') as f :
                self.p2i = json.load(f)
            for i in self.p2i.keys() :
                #
                if type(i) in [str, unicode] :
                    self.p2i[int(i)] = self.p2i.pop(i)
                    #
                #
            #    
        else : return None
        #
    #
    def genkeypair ( self, mode=0 ) :
        if mode in [0] : # Take that!
            #
            w = len(self.private)
            x = SR().choice(self.p0i.keys())
            y = SR().choice(self.p1i.keys())
            z = SR().choice(self.p2i.keys())
            self.private[w] = self.p0i[x], self.p1i[y], self.p2i[z],self.p1
            self.public[w] = x * y * z, self.p2
            #
        #
    #
    def padp0 ( self, mod, bit_sz=16 ) :
        x = 1 + SR().getrandbits(bit_sz)
        return (x * (mod -1))
    #
    def encrypt ( self, pubkey, data=None ) :
        #
        if data != None :
            #
            x, y = pubkey[0], pubkey[1]
            # isolate padp functionality
            # because it is broke as fuck
            data = self.padp0(self.p0) + data
            print data
            self.cipher[len(self.cipher)] = (data * x) % y
            return data
        print "Data must be an integer, between 1 and 16."
        print "(Data is not padded in any secure way.)"
        while 1 :
            data = long(raw_input("Data : "))
            if type(data) in [int, long] :
            #if 0 < data < self.p0 :
                x, y = pubkey[0], pubkey[1]
                self.cipher[len(self.cipher)] = (data * x) % y
                break
            else : print "Data must be an integer, between 1 and 16."
        #
    #
    def decrypt ( self, data, seckey ) :
        c = (data * seckey[2]) % self.p2 #Is in corresponding public key.
        c = (c * seckey[1]) % seckey[3] #Shh... It's a secret
        c = (c * seckey[0]) % self.p0 #Known...
        print c
        return c
        #
    #
"""    def test ( self, x, y, z=5 ) :
        ret = {}
        #while 1 :
        for i in P64 :
            if y % i == 0 : ret[x*i] = y // i
            #z -= 1
            #if z == 0 : return ret #break
        return ret
    #
    def extend ( self, x=1 ) :
        for n in range(0,x) :
            for i in self.p0mmi.keys() :
                if i > 1 :
                    a.p0mmi.update(a.test(i, a.p0mmi[i]))
                    a.p0mmi.update(a.test(a.p0mmi[i],i))
            #for i in self.p0mmi.values() :
                #if 
                #
            #
        print len(self.p0mmi)
        #
"""
# I need to dig thru the above ^^^

if __name__ == '__main__' :
    a = Triprime()
    #
    print "Do: a.p2i = findmmi(a.p2)"
    print "It might take a while..."
    b = raw_input('Do it?(Y/n)?')
    if b.lower() in ['n','no'] :
        pass
    else : a.p2i = findmmi(a.p2)
    print "Generating keypair: a.private, a.public dictionaries."
    a.genkeypair()
    print "Private: ", a.private
    print "Public: ", a.public
    print "Testing encryption..."
    a.encrypt(a.public[0])
    print "Ciphertext: ", a.cipher
    a.decrypt(a.cipher[0],a.private[0])   
    #
