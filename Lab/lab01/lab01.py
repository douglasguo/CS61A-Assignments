def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    digits = [int(d) for d in str(n)]
    if k < len(digits):
        return digits [-k-1]
    else:
        return 0

def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    arr = [a,b,c]
    sorted_arr = sorted ( arr )
    return sorted_arr [1]


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    falling_fac = n
    while k > 1:
        falling_fac = falling_fac * (n-1)
        n = n - 1
        k = k - 1
    if k >=1:
        return falling_fac
    else:
        return 1

def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    range_n = [i+1 for i in range(n)]
    divisible = 0
    for i in range_n:
        if i % k == 0:
            print(i)
            divisible = divisible + 1
    return divisible 


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    all_digits = [int(i) for i in str(y)]
    return sum(all_digits)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    all_digits = [int(i) for i in str(n)]
    if len(all_digits) == 1:
        return False
    i = 0
    while i < len(all_digits) :
        if all_digits[i] == 8:
            if all_digits[i+1] == 8:
                return True
        i = i + 1
    return False

