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
