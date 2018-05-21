# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.46(pre-alpha-crapware)


# Global sigils
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]

VALID_SIZES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_SIZES ]

DERP = [ "Invalid mode.", "Invalid public key.", "Invalid public mmi product.",
         "Invalid public prime.", "Invalid data type; Expected long.",
         "Data input too large.", "Data input too small to secure.",
         "No valid nonce available.", "Invalid private key.", "Invalid input.",
          ]

# Global rituals
#
# a long to a hex string (must .decode('hex') to restore.)
def long2str( x ) :
    if type(x) in [long] :
        ret = hex(x)[2:-1]
        if len(ret) & 1 == 1 : # This shouldn't be necessary...
            ret = '0' + ret
        return ret
    return 0
#
# a hexadecimal str to a long...
def str2long( x ) :
    if type(x) in [str] :
        return long(x,16)
    return 0
#
#
class DecryptConMan ( ) : # Context Manager... not... dammit!
    def __init__ ( self, size=VALID_SIZES[0] ) :
        if size not in VALID_SIZES : return DERP[0]
        # Assign known P0 and setup attributes
        self.P0 = PRIMES[VALID_SIZES.index(size)]
        self.size = (self.P0 - 2).bit_length()
        self.nonce_sz = self.size >> 3
        self.nonces = [ long(0) for i in range(self.nonce_sz >> 1) ]
        self.data_sz = self.size - self.nonce_sz
        self.public, self.private, self.cipher, self.data = {}, {}, {}, {}
        #
    #
    #
    def __enter__ ( self ) :
        pass
    #
    #
    def __exit__ ( self , etype, eblah, blahblah ) :
        return False
    #
    #
    def remove_nonce ( self, data ) :
        #
        if type(data) not in [long] : return DERP[4]
        if data.bit_length() > self.size : return DERP[5]
        data = long2str(data)
        if data in [0] : return DERP[9]
        return str2long(data[: -(self.nonce_sz >> 2)])
    #
    # returns a key in self.private corresponding to the private key
    def load_key ( self, seckey ) :
        if len(seckey) != 5 : return DERP[8]
        if long not in [type(i) for i in seckey] : return DERP[8]
        ret = len(self.private)
        self.private[ret] = seckey
        return ret
    #
    # returns a key in self.cipher corresponding to the ciphertext
    def load_cipher ( self, cipher ) :
        if type(cipher) not in [long] : return DERP[4]
        ret = len(self.cipher)
        self.cipher[ret] = cipher
        return ret
    #
    # returns a key in self.data corresponding to the unencrypted data
    def decrypt_cm ( self, seckey=0, cipher=0 ) :
        ret = len(self.data)
        v,w,x,y,z = ( self.private[seckey][0], self.private[seckey][1],
                      self.private[seckey][2], self.private[seckey][3],
                      self.private[seckey][4] )
        data = self.cipher[cipher]
        data = (data * v) % w
        data = (data * x) % y
        data = (data * z) % self.P0
        data = self.remove_nonce(data)
        self.data[ret] = data
        return ret
    #
    #
    def decrypt ( self, seckey, data, mode=1 ) :
        #
        if mode not in [ 0, 1 ] : return DERP[0]
        if len(seckey) != 5 : return DERP[8]
        #if set(type(i) for i in seckey) != set([long,int]) : return DERP[8]
        if long not in [type(i) for i in seckey] : return DERP[8]
        if type(data) not in [long] : return DERP[4]
        #
        if mode == 0 :
            #
            di = len(self.data)
            v,w,x,y,z = seckey[0], seckey[1], seckey[2], seckey[3], seckey[4]
            data = (data * v) % w
            data = (data * x) % y
            data = (data * z) % self.P0
            self.data[di] = data
            return di
        #
        if mode == 1 :
            #
            di = len(self.data)
            v,w,x,y,z = seckey[0], seckey[1], seckey[2], seckey[3], seckey[4]
            data = (data * v) % w
            data = (data * x) % y
            data = (data * z) % self.P0
            data = self.remove_nonce(data)
            self.data[di] = data
            return di
