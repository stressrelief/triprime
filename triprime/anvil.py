# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)

#
#import os

VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

DERP = [ "Invalid mode.",
    ]

#
# Global rituals
#

class BrimstoneAnvil ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0-2).bit_length()
        self.public, self.private, self.cipher = {}, {}, {}
        #
    #
    #
    def exportkeys ( self, file_name, k_index=0 ) :
        if type(file_name) in [str] :
            f = open(file_name + '.public.json', 'w')
            json.dump(self.public[k_index], f)
            f.close()
            f = open(file_name + '.secret.json', 'w')
            json.dump(self.private[k_index], f)
            f.close()
    #
    #
    def exportciphertext ( self, file_name, k_index=0 ) :
        if type(file_name) in [str] :
            f = open(file_name + '.cipher.json', 'w')
            json.dump(self.cipher[k_index], f)
            f.close()
    #
    #
    def importpubkey ( self, file_name ) :
        ki = len(self.public)
        if type(file_name) in [str] :
            f = open(file_name, 'r')
            self.public[ki] = tuple(json.load(f))
            f.close()
    #
    #
    def importseckey ( self, file_name ) :
        ki = len(self.private)
        if type(file_name) in [str] :
            f = open(file_name, 'r')
            self.private[ki] = tuple(json.load(f))
            f.close()
    #     
    #
    def importciphertext ( self, file_name ) :
        ki = len(self.cipher)
        if type(file_name) in [str] :
            f = open(file_name, 'r')
            self.cipher[ki] = long(json.load(f))
            f.close()
            #

