def fact(n):
    '''
    Caculate 乘积
    :param n: n>0
    :return:

    >>> fact(1)
    1
    >>> fact(4)
    24
    >>> fact(5)
    120
    '''
    if n<0:
        raise ValueError(f"invalid value {n}")
    elif n==1:
        return 1
    else:
        return fact_iter(n,1)
def fact_iter(n,r):
    if n==1:
        return r
    return fact_iter(n-1, n*r)

if __name__ == '__main__':
    import doctest
    doctest.testmod()