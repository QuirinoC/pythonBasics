while True:
    a = input('a: ')
    if not a.isnumeric(): break
    b = input('b: ')
    if not b.isnumeric(): break
    if  ( int(a) + int(b) ) > 10: break
        