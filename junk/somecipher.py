from hashlib import pbkdf2_hmac, sha512



def SBSMA ( in_ls, intk_ls ) :
    if len(in_ls) == len(intk_ls) :
        return [ ((in_ls[i]+intk_ls[i])%256) for i in range(0,len(in_ls)) ]
    else : return "Input list length mismatch."

def SBSMS ( in_ls, intk_ls ) :
    if len(in_ls) == len(intk_ls) :
        return [ ((in_ls[i]-intk_ls[i])%256) for i in range(0,len(in_ls)) ]
    else : return "Input list length mismatch."

def SBXOR ( in_ls, intk_ls ) :
    if len(in_ls) == len(intk_ls) :
        return [ (in_ls[i] ^ intk_ls[i]) for i in range(0,len(in_ls)) ]
    else: return "Input list length mismatch."

def CLSBR ( in_ls, intk ) :
    iv = intk % 8
    hmsk = (( 65280 >> iv ) & 65280 )
    lmsk = (( 65280 >> iv ) & 255 )
    return [ int(((((in_ls[i] << 8) >> iv) & hmsk) >> 8) | \
                 (((in_ls[i] << 8) >> iv) & lmsk)) for i in \
             range(0, len(in_ls)) ]

def CLSBL ( in_ls, intk ) :
    iv = intk % 8
    hmsk = (( 255 << iv ) & 65280 )
    lmsk = (( 255 << iv ) & 255 )
    return [ int((((in_ls[i] << iv) & hmsk) >> 8) | \
                 ((in_ls[i] << iv) & lmsk)) for i in \
             range(0, len(in_ls)) ]

def CLSSR ( in_ls, intk ) :
    ret = []
    tv = len(in_ls)
    iv = intk % (tv >> 1)
    for i in range(0, len(in_ls)) :
        if i == 0 :
            ret.append((((in_ls[tv-1] << 8) + in_ls[i]) >> iv) & 255)
        else :
            ret.append((((in_ls[i-1] << 8) + in_ls[i]) >> iv) & 255)
    return ret

def CLSSL ( in_ls, intk ) :
    ret = []
    tv = len(in_ls)
    iv = intk % (tv >> 1)
    for i in range(0, len(in_ls)) :
        if i == (tv - 1) :
            ret.append(((((in_ls[i] << 8) + in_ls[0]) << iv) & 65280) >> 8)
        else :
            ret.append(((((in_ls[i] << 8) + in_ls[i+1]) << iv) & 65280) >> 8)
    return ret

def TRNAP ( in_ls, intk_ls ) :
    al = [ (intk_ls[i] & 15) for i in range(0,len(intk_ls)) ]
    ah = [ ((intk_ls[i] & 240) >> 4) for i in range(0,len(intk_ls)) ]
    trnls = al + ah
    for i in range(0, len(trnls)) :
        if trnls[i] == 15 :
            in_ls.append(in_ls.pop(0))
        else :
            in_ls.append(in_ls.pop(trnls[i]))
    return in_ls

def TRNPR ( in_ls, intk_ls ) :
    al = [ (intk_ls[i] & 15) for i in range(0,len(intk_ls)) ]
    ah = [ ((intk_ls[i] & 240) >> 4) for i in range(0,len(intk_ls)) ]
    trnls = al + ah
    for i in range(0, len(trnls)) :
        if trnls[i] == 0 :
            in_ls.insert(0,in_ls.pop())
        else :
            in_ls.insert(0,in_ls.pop(trnls[i]))
    return in_ls

def TRNEI ( in_ls, intk_ls ) : #reverse TRNAP
    al = [ (intk_ls[i] & 15) for i in range(0,len(intk_ls)) ]
    ah = [ ((intk_ls[i] & 240) >> 4) for i in range(0,len(intk_ls)) ]
    trnls = al + ah
    trnls.reverse()
    for i in range(0, len(trnls)) :
        if trnls[i] == 15 :
            in_ls.insert(0,in_ls.pop())
        else :
            in_ls.insert(trnls[i],in_ls.pop())
    return in_ls

def TRNSI ( in_ls, intk_ls ) : # reverse TRNPR
    al = [ (intk_ls[i] & 15) for i in range(0,len(intk_ls)) ]
    ah = [ ((intk_ls[i] & 240) >> 4) for i in range(0,len(intk_ls)) ]
    trnls = al + ah
    trnls.reverse()
    for i in range(0, len(trnls)) :
        if trnls[i] == 0 :
            in_ls.append(in_ls.pop(0))
        else :
            in_ls.insert(trnls[i],in_ls.pop(0))
    return in_ls

def Ints2Chrs ( in_ls ) :
    return [ chr(i) for i in in_ls ]

def Chrs2Str ( in_ls ) :
    ret = ''
    for i in in_ls : ret = ret + i
    return ret

def Ints2Str ( in_ls ) :
    ret = Ints2Chrs(in_ls)
    return Chrs2Str(ret)

def Str2Ints ( in_ls ) :
    return [ int(i.encode("hex"),16) for i in in_ls ]

if __name__ == '__main__' :
    pass
