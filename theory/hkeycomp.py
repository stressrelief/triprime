#Key compression tests




def test0 ( x ) :
    base = (2,3,5,7)
    ret = []
    for i in base : # Magic prime lol
        n, e = 1, 0
        while n < x :
            n = n * i
            e += 1
        ret.append(e)
    return ret

def test1 ( x ) : # Input a list of 4 values
    if type(x) != list : return "E0"
    if len(x) != 4 : return "E1"
    base = (2,3,5,7)
    n = [ base[i]**x[i] for i in range(4) ]
    return n[0] * n[1] * n[2] * n[3]

def test2 ( x, y ) : # x integer as test0; y list of 4 values as test1
    if type(y) != list : return "E0"
    if len(y) != 4 : return "E1"
    # First, we compare bit lengths to drive stuff down quickly
    xbl = long(x).bit_length()
    ybl = sum(y)
    if ybl > xbl : # Cut it all in half... it's still too big
        if ybl / 2 > xbl : y = [ i / 2 for i in y ]
    ybl = sum(y)
    if ybl > xbl : # Try reducing the 2s exponent
        y[0] = y[0] / 2
    # now y bit length will be calculated (correctly) as the product bl
    ybl = test1(y).bit_length()
    if ybl > xbl : # Try reducing the 3s exponent
        y[1] = y[1] / 2
    ybl = test1(y).bit_length()
    if ybl > xbl : # Try reducing the 5s exponent
        y[2] = y[2] / 2
    ybl = test1(y).bit_length()
    if ybl > xbl : # Try reducing the 7s exponent
        y[3] = y[3] / 2
    ybl = test1(y).bit_length()
    if ybl > xbl : # Try reducing the 2s exponent again
        y[0] = y[0] / 2
    # No more bit lengths... now actual values will be compared
    ybl = test1(y)
    if ybl > xbl :
        y[3] -= 1
    ybl = test1(y)
    if ybl > xbl :
        y[2] -= 1
    ybl = test1(y)
    if ybl > xbl :
        y[1] -= 1
    ybl = test1(y)
    if ybl > xbl :
        y[0] -= 1
    return y

def test3 ( x, y ) :
    if type(y) != list : return "E0"
    if len(y) != 4 : return "E1"
    if test1(y) > x : return "E2"
    # Now we can work with a y product that is less than x
    D = {} # A new dict to store differentials for different y products
    Y = y[::] # A copy of y to reference
    r = [ (i / 2)+1 for i in y ]
    for i in range(0, r[3]) :
        D[x - test1(y)] = y
        print y
        y[3] += 1
        for i in range(0, r[2]) :
            D[x - test1(y)] = y
            print y
            y[2] += 1
            for i in range(0, r[1]) :
                D[x - test1(y)] = y
                print y
                y[1] += 1
                for i in range(0, r[0]) :
                    D[x - test1(y)] = y
                    print y
                    y[0] += 1
                    #
                #
            #
        #
    #
    return D

def test4 ( x, y, z ) :
    #Provide the target value to compress, x...
    #the high exponent list, y, and minimum exponent list z
    if type(y) != list : return "E0"
    if type(z) != list : return "E0"
    if len(y) != 4 : return "E1"
    if len(z) != 4 : return "E1"
    if test1(z) > x : return "E2"
    #All the inputs are somewhat sane
    ret = {}
    for i in range(z[3],y[3]) :
        for j in range(z[2],y[2]) :
            for k in range(z[1],y[1]) :
                for l in range(z[0],y[0]) :
                    # 2's exponent
                    w = test1([l,k,j,i])
                    if w < x :
                        ret[ x - w ] = (long(x-w).bit_length(),(l,k,j,i), w)
                #
            #
        #
    best = min(ret)
    print(ret[best])
    return ret
