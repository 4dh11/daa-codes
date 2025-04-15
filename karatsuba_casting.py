def karatsuba(x, y):

    if x < 10 or y < 10:
        return x*y
    
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))
    mid = n//2

    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    a = int(x_str[:-mid] or 0)
    b = int(x_str[-mid:] or 0)
    c = int(y_str[:-mid] or 0)
    d = int(y_str[-mid:] or 0)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    ac_str = str(ac) + "0"*(2 * mid)
    ad_plus_bc_str = str(ad_plus_bc) + "0"*(mid)
    return int(ac_str) + int(ad_plus_bc_str) + (bd)

if __name__ == "__main__":
    x = 3343
    y = 1619
    product = karatsuba(x, y)
    print(f"Product of {x} and {y} is: {product}")
    print(f"Verification: {x * y}")  # Should match