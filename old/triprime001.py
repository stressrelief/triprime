
from random import SystemRandom as SR

#

# Global vars
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

P32 = (2**256)+1
# Global funcs


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
# Everything below this comment is probably trash.
class MC ( ) :
    def __init__ ( self, data_sz=32 ) :
        # P32 is a global 'prime' able to encapsulate the data segment.
        # p0 is a secret 'prime' that encodes the data in a known way...
        # while allowing space for a sufficient random segment. p0, ...
        # and probably its `mmi can be exposed in the public key, as ...
        # long as the encoding scheme is stored privately. This would...
        # mean multiplication by p0(mmi,`mmi) during encryption.
        # p1 is an exposed 'prime' that is used for modular reduction...
        # of the encoded segments. Its `mmi is private.
        # Public: p0(mai),P32(mmi,`mmi) * p0(mmi) * p1(mmi),p1
        # Private: p0(`mai),p0(`mmi) * p1(`mmi),scheme
        if type(data_sz) in [int, long] :
            # 256 bits, to be used with P32
            x = ((data_sz+32) * 4)
            # 512 - 1024 bit range for p0 generation
            self.p0min = x * 2
            self.p0max = self.p0min * 2
            # 2048 - 4096 bit range for p1 generation
            self.p1min = self.p0max * 2
            self.p1max = self.p1min * 2
            #
        else : return None
        #
    #
    def test ( self, x, y, z=5 ) :
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
if __name__ == '__main__' :
    a = MC()
    a.GenerateP0()
    print len(a.p0mmi)
    #
    #for i in a.p0mmi.keys() :
        #if i > 1 :
            #a.p0mmi.update(a.test(i, a.p0mmi[i]))
    #
    #print len(a.p0mmi)
# Diarrhea... all of it...            
