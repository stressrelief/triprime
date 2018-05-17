# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.45(pre-alpha-crapware)

#
#import os
import json

VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

PATHS = { 'prv' : './triprime/private/',
          'pub' : './triprime/public/',
          'inc' : './triprime/incoming/',
          'out' : './triprime/outgoing/' }

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
    def export_public_key ( self, pubkey, filename ) :
        if len(pubkey) != 2 : return "Invalid public key."
        if long not in [type(i) for i in pubkey] : return "Invalid public key."
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        #
        path = PATHS['pub'] + filename + '.public'
        with open(path, 'w') as f :
            json.dump(pubkey, f)
            f.close()
        if f.closed in [False] : f.close() # Why not
        return path
    #
    #
    def export_private_key ( self, seckey, filename ) :
        if len(seckey) != 5 : return "Invalid private key."
        if long not in [type(i) for i in seckey] : return "Invalid private key."
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        #
        path = PATHS['prv'] + filename + '.secret'
        with open(path, 'w') as f :
            json.dump(seckey, f)
            f.close()
        if f.closed in [False] : f.close() # Why not
        return path 
    #
    #
    def export_ciphertext ( self, cipher, filename ) :
        #if len(cipher) != 1 : return "Invalid ciphertext."
        if long not in [type(cipher)] : return "Invalid ciphertext."
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        #
        path = PATHS['out'] + filename + '.cipher'
        with open(path, 'w') as f :
            json.dump(cipher, f)
            f.close()
        if f.closed in [False] : f.close() # Why not
        return path 
    #
    #
    def import_public_key ( self, filename ) :
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        ki = len(self.public)
        path = PATHS['inc'] + filename + '.public'
        with open(path, 'r') as f :
            self.public[ki] = tuple(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki
    #
    #
    def import_private_key ( self, filename ) :
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        ki = len(self.private)
        path = PATHS['inc'] + filename + '.secret'
        with open(path, 'r') as f :
            self.private[ki] = tuple(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki
    #     
    #
    def import_secrets ( self, filename ) :
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        ki = len(self.private)
        path = PATHS['prv'] + filename + '.secret'
        with open(path, 'r') as f :
            self.private[ki] = tuple(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki
    #
    #
    def import_ciphertext ( self, filename ) :
        if type(filename) not in [str] : return "Invalid filename."
        if len(filename) >= 64 : return "Filename too long."
        ki = len(self.cipher)
        path = PATHS['inc'] + filename + '.cipher'
        with open(path, 'r') as f :
            self.cipher[ki] = long(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki

