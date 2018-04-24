# reverse integer ,given a 32-bit signed int, reverse digits of an int
def reverse(x):
    ''' input type: int
        rtype: int
        '''
    is_nagative = 1
    reverse_int = 0
    if x < 0:
        is_nagative = -1
        x *= -1
    while x > 0:
        remainder = x % 10
        x //= 10
        reverse_int = reverse_int * 10 + remainder
    reverse_int *= is_nagative
    if reverse_int > 2 ** 31 - 1 or reverse_int < - 2 ** 31:
        return 0
    return reverse_int
        
