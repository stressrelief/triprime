# Begotten of Assymetricyptogorgonomicron
# v: 0.0.1.46(pre-alpha-crapware)

import triprime.forge as forge    # Key/nonce generation
import triprime.anvil as anvil    # Simple file I/O (json)
import triprime.hammer as hammer   # Enc./Dec. modes

# Global sigils
VALID_MODES = (32,64,128,256,512,1024)

PRIMES = [ (2**i)+1 for i in VALID_MODES ]

DERP = [ "Invalid mode.", "Nonce generation failed.",
         "Failed to generate key primitives.",
          ]

# Global rituals
#
# Profile dict { 0 : [ name, mode, prvki, pubki, keyage, [prv_file_ls], [pub_file_ls] ] }
#
class TriPrime ( ) :
    def __init__ ( self, mode=32 ) :
        if mode not in VALID_MODES : return DERP[0]
        # Assign known P0 and setup attributes
        self.mode = mode
        self.P0 = PRIMES[VALID_MODES.index(mode)]
        self.size = (self.P0 - 2).bit_length()
        #
    #
    # given a file name, load that file using the .import_secrets method from anvil
    # if given a tuple/list, load all files that match string prefixes in the list
    # ret anvil
    def load_secrets ( self, file_ls ) :
        if type(file_ls) not in [list, str, tuple] : return "Invalid input."
        if type(file_ls) in [str] :
            ret = anvil.BrimstoneAnvil(self.mode)
            i = ret.import_secrets(file_ls)
            if i in anvil.DERP : return i
            return ret
        if type(file_ls) in [list, tuple] :
            ret = anvil.BrimstoneAnvil(self.mode)
            for i in file_ls :
                if type(i) in [str] :
                    j = ret.import_secrets(i)
                    if j in anvil.DERP : return j
            return ret
        #
    #
    # ret anvil
    def load_publics ( self, file_ls ) :
        if type(file_ls) not in [list, str, tuple] : return "Invalid input."
        if type(file_ls) in [str] :
            ret = anvil.BrimstoneAnvil(self.mode)
            i = ret.import_publics(file_ls)
            if i in anvil.DERP : return i
            return ret
        if type(file_ls) in [list, tuple] :
            ret = anvil.BrimstoneAnvil(self.mode)
            for i in file_ls :
                if type(i) in [str] :
                    j = ret.import_publics(i)
                    if j in anvil.DERP : return j
            return ret
        #
    #
    # ret anvil
    def load_incoming ( self, file_ls ) :
        if type(file_ls) not in [list, str, tuple] : return "Invalid input."
        if type(file_ls) in [str] :
            ret = anvil.BrimstoneAnvil(self.mode)
            i = ret.import_ciphertext(file_ls)
            if i in anvil.DERP : return i
            return ret
        if type(file_ls) in [list, tuple] :
            ret = anvil.BrimstoneAnvil(self.mode)
            for i in file_ls :
                if type(i) in [str] :
                    j = ret.import_ciphertext(i)
                    if j in anvil.DERP : return j
            return ret
    #
    # Given a forge/anvil , import nonces, public, and private keys
    # ret hammer
    def enchant_hammer ( self, target ) :
        ret = hammer.BaleHammer(self.mode)
        for i in target.private :
            ret.private[len(ret.private)] = target.private[i]
        for i in target.public :
            ret.public[len(ret.public)] = target.public[i]
        try :
            ret.nonces = target.nonces
        except AttributeError as ex :
            x = forge.HellForge(self.mode)
            x.gen_nonces()
            ret.nonces, ret.nonce_sz = x.nonces, x.nonce_sz
        return ret
    #
    # ret hammer
    def forge_hammer ( self, ) :
        #
        #mode = self.mode
        a = forge.HellForge(self.mode)
        a.gen_nonces()
        b = a.check_nonces()
        if b in [False] : return DERP[1]
        b = a.gen_key_parts()
        if b in [1,2,3] : return DERP[2]
        b = a.check_key_parts()
        if b in [False] : return DERP[2]
        # perform experimental mmi extension
        #b = a.extend_key()
        #if b in [False] : return " "
        b = a.forge_keypair()
        if b in a.DERP : return b
        #
        return self.enchant_hammer(a)
    #
    # ret anvil
    def export_file ( self, filedata, filename, filetype ) :
        if type(filename) not in [str] : return "Invalid filename."
        if type(filetype) not in [str] : return "Invalid filetype."
        if filetype.lower() in ['public', 'pub'] :
            f = anvil.BrimstoneAnvil(self.mode).export_public_key(filedata, filename)
            if f in anvil.DERP : return "PKE Error: " + f
            return f
        elif filetype.lower() in ['private', 'secret', 'sec', 'prv'] :
            f = anvil.BrimstoneAnvil(self.mode).export_private_key(filedata, filename)
            if f in anvil.DERP : return "SKE Error: " + f
            return f
        elif filetype.lower() in ['profile', 'pro'] :
            f = anvil.BrimstoneAnvil(self.mode).export_profile(filedata, filename)
            if f in anvil.DERP : return "PRE Error: " + f
            return f
        elif filetype.lower() in ['ctest'] :
            f = anvil.BrimstoneAnvil(self.mode).export_ciphertest(filedata, filename)
            if f in anvil.DERP : return "CTT Error: " + f
            return f
        else :
            f = anvil.BrimstoneAnvil(self.mode).export_ciphertext(filedata, filename)
            if f in anvil.DERP : return "CTE Error: " + f
            return f
        #
    #
    #
    def _test0 ( self ) :
        # Alice
        a = TriPrime(128)
        # A hammer to decrypt with ex00 private key
        a.d0 = a.enchant_hammer(a.load_secrets('ex00'))
        # A hammer to encrypt with ex01 public key
        a.e0 = a.enchant_hammer(a.load_publics('ex01'))
        # Bob
        b = TriPrime(128)
        b.d0 = b.enchant_hammer(b.load_secrets('ex01'))
        b.e0 = b.enchant_hammer(b.load_publics('ex00'))
        #
        a.msg, b.msg = 'ASecretMessage', 'BSecretMessage'
        print a.msg
        a.data = hammer.str2long(a.msg.encode('hex'))
        a.e0.encrypt(a.e0.public[0], a.data)
        pa = a.export_file(a.e0.cipher[0], 'cta0', 'ctest')
        print pa
        #
        print b.msg
        b.data = hammer.str2long(b.msg.encode('hex'))
        b.e0.encrypt(b.e0.public[0], b.data)
        pb = b.export_file(b.e0.cipher[0], 'ctb0', 'ctest')
        print pb
    #
    #
#
if __name__ == '__main__' :
    # Alice
    foo = TriPrime()._test0()
