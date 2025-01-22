def sumacplx(a,b):
    return ((a[0]+b[0],a[1]+b[1]))

#(a1 + b1i) × (a2 + b2i) = ((a1a2) − (b1b2)) + ((a1b2) + (a2b1))i
def multcplx(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

if __name__ == '__main__':
    print(multcplx((3.5, 6), (-6.7, 2)))
    print(sumacplx((3.5, 6), (-6.7, 2)))