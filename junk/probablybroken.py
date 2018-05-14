from random import SystemRandom

from hashlib import md5, sha256, sha512

from struct import pack, unpack

#import Tkinter as tk

VERSION = 0x0101
OPTIONS = 0xffff
#

PROTOCOL = 0x0101
# -15- Reserved              -14- Reserved
# -13- TooSaltySPA           -12- Reserved DSA
# -11- SHA 256 + MD 5 MA     -10- Reserved DSA
# -09- SHA512 MA             -08- Spungash512x2 MA
# -07- Reserved              -06- 2Step BCE
# -05- AES BCE               -04- Twofish BCE
# -03- Crypt Padding         -02- Reserved
# -01- Crypt Nonces          -00- Delayed 2 way handshake

class Common ( ) :
    def __init__ ( self, fn ) :
        self.FileN = fn
        
                   
class GCO ( ) :
    def __init__ ( self, options=0xffff, protocol=0x0101 ) :
        self.a = long(self.GenPrivateA())
        self.ab = (hex(self.a)[2:-1])
        if len(self.ab) & 1 :
            self.ab = '0' + self.ab
        self.A = long(self.GenPublicA())
        self.Ab = (hex(self.A)[2:-1])
        if len(self.Ab) & 1 :
            self.Ab = '0' + self.Ab
        self.PM = long(self.GenPublicModulus())
        self.PMb = (hex(self.PM)[2:-1])
        if len(self.PMb) & 1 :
            self.PMb = '0' + self.PMb
        self.PA = long(pow(self.A,self.a,self.PM))
        self.PAb = (hex(self.PA)[2:-1])
        if len(self.PAb) & 1 :
            self.PAb = '0' + self.PAb
        self.la, self.lA = len(self.ab)/2, len(self.Ab)/2
        self.lPM, self.lPA = len(self.PMb)/2, len(self.PAb)/2
        print self.la, len(self.ab)
        #self.CheckHex()
        self.ab = bytearray.fromhex(self.ab)
        self.Ab = bytearray.fromhex(self.Ab)
        self.PMb = bytearray.fromhex(self.PMb)
        self.PAb = bytearray.fromhex(self.PAb)


    def ForgePublicKey ( self ) :
        self.PKHeader = pack('8H', VERSION, OPTIONS, PROTOCOL, 16,
                             self.lPM, self.lA, self.lPA, 128)
        self.PKBody = self.PMb + self.Ab + self.PAb
        self.PKBody = pack("%dp" % len(self.PKBody), str(self.PKBody))
        a0 = sha256(self.PKHeader).digest()
        b0 = sha256(self.PKBody).digest()
        c0 = sha512((self.PKHeader + self.PKBody)).digest()
        self.PKFooter = a0 + b0 + c0
        self.PKFooter = pack("128p", str(self.PKFooter))


    def ForgeSecretKey ( self ) :
        self.SKHeader = pack('8H', VERSION, OPTIONS, PROTOCOL, 16,
                             self.lPM, self.lA, self.la, 128)
        self.SKBody = self.PMb + self.Ab + self.ab
        self.SKBody = pack("%dp" % len(self.SKBody), str(self.SKBody))
        a0 = sha256(self.SKHeader).digest()
        b0 = sha256(self.SKBody).digest()
        c0 = sha512((self.SKHeader + self.SKBody)).digest()
        self.SKFooter = a0 + b0 + c0
        self.SKFooter = pack("128p", str(self.SKFooter))


    def FilePublicKey ( self, fn ) :
        f = open(fn, 'w')
        f.write(self.PKHeader)
        f.write(self.PKBody)
        f.write(self.PKFooter)
        f.close()
        return fn
    

    def FileSecretKey ( self, fn ) :
        f = open(fn, 'w')
        f.write(self.SKHeader)
        f.write(self.SKBody)
        f.write(self.SKFooter)
        f.close()
        return fn


    def LoadFileSKey ( self, fn ) :
        f = open(fn,'rb', 4096)
        #read first 8 bytes
        hea = f.read(8)
        hea = self.CheckHeader(hea)
        if hea == 0 :
            f.close()
            return 0
        F = Common(fn)
        F.Version, F.Options, F.Protocol, F.HeadLen = hea[0], hea[1], hea[2], hea[3]
        der = f.read((F.HeadLen-8))
        der = self.ReadHeader(der)
        F.PMLen, F.ALen, F.aLen, F.FootLen = der[0], der[1], der[2], der[3]
        body = f.read(F.PMLen)
        F.PM = self.ReadFileSKey(body, F.PMLen)
        body = f.read(F.ALen)
        F.A = self.ReadFileSKey(body, F.ALen)
        body = f.read(F.aLen)
        F.a = self.ReadFileSKey(body, F.aLen)
        del(body)
        footer = f.read(F.FootLen)
        F.Footer = self.ReadFooter(footer)
        #
        f.close()
        return F


    def LoadFilePKey ( self, fn ) :
        f = open(fn,'rb', 4096)
        #read first 8 bytes
        hea = f.read(8)
        hea = self.CheckHeader(hea)
        if hea == 0 :
            f.close()
            return 0
        F = Common(fn)
        F.Version, F.Options, F.Protocol, F.HeadLen = hea[0], hea[1], hea[2], hea[3]
        der = f.read((F.HeadLen-8))
        der = self.ReadHeader(der)
        F.PMLen, F.ALen, F.PALen, F.FootLen = der[0], der[1], der[2], der[3]
        body = f.read(F.PMLen)
        F.PM = self.ReadFileSKey(body, F.PMLen)
        body = f.read(F.ALen)
        F.A = self.ReadFileSKey(body, F.ALen)
        body = f.read(F.PALen)
        F.PA = self.ReadFileSKey(body, F.PALen)
        del(body)
        footer = f.read(F.FootLen)
        F.Footer = self.ReadFooter(footer)
        #
        f.close()
        return F



    def ReadFileSKey ( self, body, blen ) :
        print len(body), blen
        S = unpack("%dp" % blen, body)
        S = S[0]
        #print S
        return S


    def ReadFooter ( self, footer ) :
        F = unpack("%dp" % len(footer), footer)
        F = F[0]
        #print F
        return F




    def CheckHeader ( self, header ) :
        V, O, P, H = unpack('HHHH', header)
        #unpack tuple ... 
        #V, O, P, H = V[0], O[0], P[0], H[0]
        if (V != 257) | (O != 65535) | (P != 257) :
            return 0
        if H == 16 :
            return V, O, P, H
        return 0


    def ReadHeader ( self, header ) :
        A, B, C, D = unpack('HHHH', header)
        #A, B, C, D = A[0], B[0], C[0], D[0]
        return A, B, C, D
    




    def CheckHex ( self ) :
        l0 = [self.lPM, self.lA, self.lPA, self.la]
        l1 = [self.PMb, self.Ab, self.PAb, self.ab]
        for i in range(0,4) :
            if l0[i] & 1 :
                print l1[i], l0[i]
                l1[i] = hex(0)[0] + l1[i]
                l0[i] = l0[i] + 1
                print l1[i], l0[i]


                





        


    def binarygcd ( self, u, v ) :
        if u == v :
            return u
        if u == 0 :
            return v
        if v == 0 :
            return u
        if ~u & 1 : # u is even
            if v & 1 : # v is odd
                return binarygcd(u >> 1, v)
            else :
                return binarygcd(u >> 1, v >> 1) << 1
        if ~v & 1 : # u is odd, v is even
            return binarygcd(u, v >> 1)
        if u > v :
            return binarygcd((u - v) >> 1, v)
        return binarygcd((v - u) >> 1, u)


    def BinaryGCD ( self, u, v ) :
        shift = 0
        if u == 0 : return v
        if v == 0 : return u
        for i in range(0,((u | v)&1)):
            u = u >> 1
            v = v >> 1
            shift = shift + 1
        while ( u & 1 ) == 0 :
            u = u >> 1
        while v != 0 :
            while ( v & 1 ) == 0 :
                v = v >> 1
            if u > v :
                u, v = v, u
            v = v - u
        return u << shift


    def GenRandom ( self, num_bytes ) :
        return SystemRandom().getrandbits(num_bytes*8)


    def CalculateIntSum ( self, pmc ) : # input string
        while len(pmc) > 1 :
            s = 0
            for i in pmc :
                s = s + int(i)
            pmc = str(s)
        return pmc


    def CheckPrimalityWeak ( self, PM ) : # input long
        bad_ld = '024568'
        bad_ss = '369'
        check = str(PM)
        ld = check[-1:]
        if ld in bad_ld :
            return False
        ss = self.CalculateIntSum(check)
        if ss in bad_ss :
            return False
        return True


    def GenPublicModulus ( self ) :
        # 640 to 1024 bytes
        while 1:
            x = (self.GenRandom(2) & 1023) + 1
            if x > 639 :
                break
        result = False
        while result == False :
            PM = self.GenRandom(x)
            result = self.CheckPrimalityWeak(PM)
        return long(PM)


    def GenPublicA ( self ) :
        # 8 to 64 bytes
        while 1:
            x = self.GenRandom(1) + 1
            if x > 7 and x < 65 : # decent A length
                break
        result = False
        while result == False :
            A = self.GenRandom(x)
            result = self.CheckPrimalityWeak(A)
        return long(A)


    def GenPrivateA ( self ) :
        # 64 to 256 bytes
        while 1:
            x = self.GenRandom(1) + 1
            if x > 63 and x < 257 : # decent b,a length
                break
        result = False
        while result == False :
            a = self.GenRandom(x)
            result = self.CheckPrimalityWeak(a)
        return long(a)


if __name__ == '__main__' :
    X = GCO()
    X.ForgePublicKey()
    X.ForgeSecretKey()
    A = X.LoadFilePKey('pubkey123.key')
    
    
