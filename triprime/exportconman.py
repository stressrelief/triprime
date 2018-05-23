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
class ExportCM ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0-2).bit_length()
        self.public, self.private, self.cipher = {}, {}, {}
        #
    #
    #
    def export_public_key ( self, pubkey, filename ) :
        if len(pubkey) != 2 : return DERP[1]
        if long not in [type(i) for i in pubkey] : return DERP[1]
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        path = PATHS['pub'] + filename + '.public'
        with open(path, 'w') as f :
            json.dump(pubkey, f)
            f.close()
        if f.closed in [False] : f.close() # Why not
        return path
    #
    #
    def export_private_key ( self, seckey, filename ) :
        if len(seckey) != 5 : return DERP[4]
        if long not in [type(i) for i in seckey] : return DERP[4]
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        #
        path = PATHS['prv'] + filename + '.secret'
        with open(path, 'w') as f :
            json.dump(seckey, f)
            f.close()
        if f.closed in [False] : f.close() 
        return path 
    #
    #
    def export_ciphertext ( self, cipher, filename ) :
        if long not in [type(cipher)] : return DERP[5]
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        path = PATHS['out'] + filename + '.cipher'
        with open(path, 'w') as f :
            json.dump(cipher, f)
            f.close()
        if f.closed in [False] : f.close() 
        return path 
    #
    #
    def export_profile ( self, profile, filename ) :
        #
        if type(filename) not in [str] : return DERP[2]
        if len(filename) >= 64 : return DERP[3]
        path = PATHS['pro'] + filename + '.profile'
        with open(path, 'w') as f :
            json.dump(profile, f)
            f.close()
        if f.closed in [False] : f.close()
        return path
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
