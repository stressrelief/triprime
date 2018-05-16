# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)


# Global sigils
VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

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
class BaleHammer ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        # Assign known P0 and setup attributes
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0 - 2).bit_length()
        self.nonce_sz = self.size >> 3
        self.nonces = [ long(0) for i in range(self.nonce_sz >> 1) ]
        self.data_sz = self.size - self.nonce_sz
        self.public, self.private, self.cipher, self.data = {},{},{},{}
        #
    #
    #    
    def use_nonce ( self, data ) :
        #
        if type(data) not in [long] : return DERP[4]
        if data.bit_length() > self.data_sz : return DERP[5]
        if len(self.nonces) <= 0 : return 0 #
        x, y = long2str(data), long2str(self.nonces.pop())
        if x in [0] : return DERP[9]
        if y in [0] : return 0 #
        # calc the pad to keep nonce in upper bits
        z = (self.data_sz >> 2) - len(x)
        data = x + '0'*z + y
        return str2long(data)   
    #
    #
    def remove_nonce ( self, data ) :
        #
        if type(data) not in [long] : return DERP[4]
        if data.bit_length() > self.size : return DERP[5]
        data = long2str(data)
        if data in [0] : return DERP[9]
        return str2long(data[: -self.nonce_sz])
    #
    #
    def encrypt ( self, pubkey, data, mode=1 ) :
        # A simple mode for pair checking will exist temporarily
        #    Enc/Dec  Nonce   HMAC      ?
        # M 0   X
        # O 1   X       X
        # D 2   X               X  
        # E 3   X       X       X
        # S 4   ?       ?       ?       ?
        # Current support: 0,1
        if mode not in [ 0, 1 ] : return DERP[0]
        if len(pubkey) != 2 : return DERP[1]
        if type(pubkey[0]) not in [long] : return DERP[2]
        if type(pubkey[1]) not in [long] : return DERP[3]
        if 0 in [ pubkey[1] % i for i in P64 ] : return DERP[3]
        if type(data) not in [long] : return DERP[4]
        if data.bit_length() > self.data_sz : return DERP[5]
        #
        if mode == 0 :
            # Encryption and Decryption only
            di = len(self.cipher)
            x, y = pubkey[0], pubkey[1]
            self.cipher[di] = (data * x) % y
            # Security check for small data
            if self.cipher[di] / x == data : return DERP[6]
            return di
        #
        if mode == 1 :
            # Enc. / Dec. with nonce support
            if self.check_nonces() in [False] : return DERP[7]
            di = len(self.cipher)
            x, y = pubkey[0], pubkey[1]
            # Attempt to use a nonce
            data = self.use_nonce(data)
            if data in [0] : return DERP[7]
            self.cipher[di] = (data * x) % y
            # Security check for small data
            if self.cipher[di] / x == data : return DERP[6]
            return di
        #
    #
    #
    def decrypt ( self, seckey, data, mode=1 ) :
        #
        if mode not in [ 0, 1 ] : return DERP[0]
        if len(seckey) != 5 : return DERP[8]
        if set(type(i) for i in seckey) != set([long,int]) : return DERP[8]
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
        #
        

