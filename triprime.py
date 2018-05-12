
from random import SystemRandom as SR

#

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
            # Simple demonstration
            # Overrides functionality... remove.
            self.public, self.private, self.cipher = {}, {}, {}
            self.ds = 4
            self.p0 = P4
            self.p0i = findmmi(self.p0)
            self.p1 = P8 # But it's totally a secret... shh...
            self.p1i = findmmi(self.p1)
            self.p2 = P16
            #self.p2i = findmmi(self.p2)
        else : return None
        #
    #
    def genkeypair ( self, mode=0 ) :
        if mode in [0] : # Take that!
            #
            w = len(self.private)
            x = SR().choice(self.p0i)
            y = SR().choice(self.p1i)
            z = SR().choice(self.p2i)
            self.private[w] = self.p0i[x], self.p1i[y], self.p2i[z],self.p1
            self.public[w] = x * y * z, self.p2
            #
        #
    #
    def encrypt ( self, pubkey ) :
        #
        print "Data must be an integer, between 1 and 16."
        print "(Data is not padded in any secure way."
        while 1 :
            data = int(raw_input("Data : "))
            if 0 < data < self.p0 :
                x, y = pubkey[0], pubkey[1]
                self.cipher[len(self.cipher)] = (data * x) % y
                break
            else : print "Data must be an integer, between 1 and 16."
        #
    #
    def decrypt ( self, seckey ) :
        pass
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
    #
    def GenerateP0 ( self ) :
        # BS method:
        x = self.p0min + (self.p0max >> 3)
        while 1 :
            p0 = SR().getrandbits(x >> 1)
            if p0 % 2 == 1 : p0 += 1
            td = {}
            td[1] = p0
            for i in P64 :
                if p0 % i == 0 : td[i] = p0 // i
                #
            if len(td) > 1 :
                self.p0 = p0
                self.p0mmi = td
                break
            #
        #limit = len(td)
        #ret = td.copy()
        #while 1 :
        #    for i in td :
        #        if i > 1 :
        #            for n in P64 :
        #                if td[i] % n == 0 : ret[i*n] = td[i] // n
        #                else : pass
        #                #if td[i] % 2 == 0 : ret[i*2] = td[i] // 2
        #            if len(ret) == limit : break
        #            if len(ret) > limit :
        #                limit = len(ret)
        #                print limit
                        #
                    #
                #
            #
        #
        #self.p0mmi = ret
        #return limit
                    #if td[i] % 2 == 0 : td[i*2] = td[i] // 2
            # (p0 * p0) = x. check odd parity.
            # extend appropriately: [1,3,5,7] or [2,4,6,8]
            #self.p0 = p0
            #self.p0mmi = td
            # calculate extended mmi's
            #sd = td.keys()
            #ld = td.values()
            
            # BS bugs
            #print p0
            #print p0.bit_length()
            #p0 = p0 * p0
            #print p0.bit_length()
            #return p0
        
        #
    #
        #
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
    c = (a.cipher[0] * a.private[0][2]) % a.public[0][1]
    print c
    c = (c * a.private[0][1]) % a.private[0][3]
    print c
    c = (c * a.private[0][0]) % a.p0
    print c
    
    #
