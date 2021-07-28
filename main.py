def has_remainder(x, y):
    m = x % y
    if m == 0:
        return False
    else:
        return True


def find_factors ( y):
    print('Need to find factors')


l = input('L')
r = input('R')

if l > r:
    small = r
    remainder = has_remainder(l, r)
else:
    small = l
    remainder = has_remainder(r, l)

print(">>> Is there a remainder", remainder)

if not remainder:
    l_div = l/small
    r_div = r/small

    print (l_div, r_div)
else:
    find_factors(l)
