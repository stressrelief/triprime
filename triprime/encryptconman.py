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
class EncryptConMan ( ) : # Context Manager... not... dammit!
    def __init__ ( self, pubkey, target, size=VALID_SIZES[0] ) :
        if size not in VALID_SIZES : return DERP[0]
        # Assign known P0 and setup attributes
        self.P0 = PRIMES[VALID_SIZES.index(size)]
        self.size = (self.P0 - 2).bit_length()
        self.usage = 0
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
    def check_nonces ( self ) :
        #
        x, y, z = len(self.nonces), len(set(self.nonces)), self.nonce_sz >> 1
        x, y = x + self.usage, y + self.usage
        if self.usage == z : return False
        if x == y :
            if x == z :
                return True
            #
        return False
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
        #z = (self.data_sz >> 2) - len(x)
        #data = x + '0'*z + y
        data = x + y
        self.usage += 1
        return str2long(data)   
    #
    # returns a key in self.public corresponding to the public key
    def load_key ( self, pubkey ) :
        if len(pubkey) != 2 : return DERP[1]
        if type(pubkey[0]) not in [long] : return DERP[2]
        if type(pubkey[1]) not in [long] : return DERP[3]
        if 0 in [ pubkey[1] % i for i in P64 ] : return DERP[3]
        ret = len(self.public)
        self.public[ret] = pubkey
        return ret
    #
    # returns a key in self.data corresponding to the data
    def load_data ( self, data ) :
        if type(data) not in [long] : return DERP[4]
        if data.bit_length() > self.data_sz : return DERP[5]
        ret = len(self.data)
        self.data[ret] = data
        return ret
    #
    # returns a key in self.cipher corresponding to the ciphertext
    def encrypt_cm ( self, pubkey=0, data=0 ) :
        if self.check_nonces() in [False] : return DERP[7]
        ret = len(self.cipher)
        x, y = self.public[pubkey][0], self.public[pubkey][1]
        # Attempt to use a nonce
        data = self.use_nonce(self.data[data])
        if data in [0] : return DERP[7]
        self.cipher[ret] = (data * x) % y
        # Security check for small data
        if self.cipher[ret] / x == data : return DERP[6]
        return ret
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
