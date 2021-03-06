"""
Provides functions to compute the greatest common divisor between two numbers.

Provides functions to compute the greatest common divisor between two numbers.
"""


DEBUG = True

def gcd1(a, b):
    if DEBUG: print(f"GCD1: a={a} b={b}")
    if b == a:
        return(a)
    elif b > a:
        return(gcd1(b, a))
    return(gcd1(a - b, b))


def gcd2(a, b):  # correct a potential problem in version 1
    if DEBUG: print(f"GCD2: a={a} b={b}")
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a > 0
    assert b > 0
    return gcd1(a, b)


def gcd3(a, b):  # uses the modulo 'trick'
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a > 0
    assert b > 0
    if DEBUG: print(f"GCD3: a={a} b={b}")

    if a == 0:
        return(b)
    elif b > a:
        return(gcd3(b, a))
    c = a % b  # c is the remainder of the integer division of a by b
    if c == 0:
        return b
    else:
        return(gcd3(b, c))

def gcd4(a, b):  # non recursive version
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a > 0
    assert b > 0
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, (a % b)
        if DEBUG: print(f"GCD4: a={a} b={b}")
    return a
    

# It is also possible to use a lambda:
gcd5 = lambda a, b: a if not b else gcd5(b, a % b)


if __name__ == '__main__':
    a = 12
    b = 16
    print("gcd1({}, {}) = {}".format(a, b, gcd1(a, b)))
    print("gcd2({}, {}) = {}".format(a, b, gcd2(a, b)))
    print("gcd3({}, {}) = {}".format(a, b, gcd3(a, b)))
    print("gcd4({}, {}) = {}".format(a, b, gcd4(a, b)))
    print("gcd5({}, {}) = {}".format(a, b, gcd5(a, b)))
