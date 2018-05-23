# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.46(pre-alpha-crapware)

#
#import os
import json

VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

PATHS = { 'prv' : './triprime/private/',
          'pub' : './triprime/public/',
          'inc' : './triprime/incoming/',
          'out' : './triprime/outgoing/',
          'pro' : './triprime/profiles/'}

DERP = [ "Invalid mode.", "Invalid public key.", "Invalid filename.",
         "Filename too long.", "Invalid private key.", "Invalid ciphertext.",
    ]

#
# Global rituals
#
class ImportCM ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0-2).bit_length()
        self.public, self.private, self.cipher = {}, {}, {}
        #
    #
    #
    def __enter__ ( ) :
        pass
	#
	#
    def __exit__ ( e, err, etb ) :
        return False
    #
    # exports to incoming for easy importing
    def export_ciphertest ( self, cipher, filename ) :
        if long not in [type(cipher)] : return DERP[5]
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        path = PATHS['inc'] + filename + '.cipher'
        with open(path, 'w') as f :
            json.dump(cipher, f)
            f.close()
        if f.closed in [False] : f.close() 
        return path
    #
    #
    def import_public_key ( self, filename ) :
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
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
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
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
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        ki = len(self.private)
        path = PATHS['prv'] + filename + '.secret'
        with open(path, 'r') as f :
            self.private[ki] = tuple(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki
    #
    #
    def import_publics ( self, filename ) :
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        ki = len(self.public)
        path = PATHS['pub'] + filename + '.public'
        with open(path, 'r') as f :
            self.public[ki] = tuple(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki
    #
    #
    def import_ciphertext ( self, filename ) :
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        ki = len(self.cipher)
        path = PATHS['inc'] + filename + '.cipher'
        with open(path, 'r') as f :
            self.cipher[ki] = long(json.load(f))
            f.close()
        if f.closed in [False] : f.close()
        return ki

