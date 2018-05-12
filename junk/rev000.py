
from random import SystemRandom as SR
#

#Global vars
P64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
       139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
       223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
       293, 307, 311]




#Global functions
def findmmi ( prime, x=None ) :
    a = prime - 1
    b = prime + 1
    if x != None :
        c = (b // x) - 1 # c = 2
        if c == 0 :
            c = b // 2
            print c, prime, (prime - c), b.bit_length()
            while (x * c) % prime != 1 :
                c -= 1
                if c < 2 : return "Error0"
            return c
        print c, prime, (prime - c), b.bit_length()
        while (x * c) % prime != 1 :
            c += 1
            if c > prime : return "Error1"
        return c
    #
        
    c,d = [i for i in range(2,b)], [i for i in range(2,b)]
    ret = {}
    if ( a * a ) % prime == 1 :
        ret[a] = a
        # Modified for test2 function testing
        ret[0] = prime
        #
        c.remove(a)
        d.remove(a)
    else : return "Not prime."
    for i in c :
        for n in d :
            if ( i * n ) % prime == 1 :
                ret[i] = n
                d.remove(n)
                #d.remove(i)
                break
            #
        #
    #
    return ret
    #
#

#
def test0 ( bitsz ) :
    #simple: 8b + 8b + 8b = 24b
    #128 DATA + 32 = 160 DATA, 128 RAND, *6
    if type(bitsz) in [int, long] :
        # select a value within the available range for p0
        a = SR().randrange((bitsz*2)+2,(bitsz*3)+4)
        # attempt to generate a potential p0 of bit size a
        while 1 :
            b = SR().getrandbits(a)
            if b.bit_length() == a : break
            #
        # see if b is odd and adjust as necessary
        if b & 1 == 0 : b = b + 1
        if b.bit_length() > a : b = b - 2
        # begin testing for primality of b
        # divisible by first 64 primes?
        while 1 :
            z = [(b % i) for i in P64]
            if 0 in z : b += 2
            else : break
        # generate mmi after eliminating some composites (above P64)
        r = SR().getrandbits(a // 2)
        c = findmmi(b, r) # breaks the world
        while 1 :
            if type(c) == str :
                b = b + 2
                c = findmmi(b, r) # infinite loop + processor intensive?! Sign me up!
            #
            if type(c) == long : break
            #
        #
        return a,b,c,r
    return 0
#
def test1 ( count ) :
    if type(count) in [int, long] :
        ret = []
        while count > 0 :
            ret.append(test0(6))
            count -= 1
        return ret
    if type(count) in [list, tuple, set] :
        ret = []
        for i in count :
            ret.append(test0(i))
        return ret
    #
#
def test2 ( p0, p1 ) :
    ret = {}
    if type(p0) in [ dict ] and type(p1) in [ dict ] :
        #
        x, y = p0.pop(0), p1.pop(0)
        if x > y : lo, hi, data = p1, p0, y
        else : lo, hi, data = p0, p1, x
        p = 0
        #
        a, b = lo.values(), lo.keys()
        c, d = hi.values(), hi.keys()
        print len(a), len(b), len(c), len(d), data
        for blah in range(0,len(hi)) : ret[blah] = []
        for n in hi :
            for i in range(0, data-2) :
                t0 = i*a[i]*c[i]
                t1 = t0*b[i]*d[i]
                ret[p].append([[ i, a[i],b[i],c[i],d[i]],
                               [ t0, t1, t1 % x, t1 % y ]])
            p += 1
        return ret
#61 313 252 9
#415 4583 4168 13
#5259 2220041 2214782 22
#39105 826741259 826702154 30
#[(8, 313L, 188L, 5L), (13, 4583L, 1250L, 11L), (22, 2220041L, 615509L, 422L), (30, 826741259L, 292161390L, 21141L)]
# generate 2 n-bit values.
# make them prime
# use (2**r0 * 3**r1 * p0**r2 * p1**r3)
# use the composite's known construction to make MMIs
# check primality of this new composite - 1
# Hah, more old shit...
