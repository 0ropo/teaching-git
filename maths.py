

def div(a, b):
    """
    a and b must be float
    Compute the quotient of two numbers

    >>> div(6, 2)
    3.0
    >>> div(3, -1)
    -3.0
    """
    if b == 0:
        raise DivisionByZeroError()
    return a / b

def mumul(a, b):
    """
    a and b should be objects having dmethode
    Compute the product of two numbers

    >>> mul(3, 2)
    6
    >>> mul(3, 0)
    0
    >>> mul(-1, 5)
    -5
    """
    m = 0
    for _ in range(b):
        m += a
    return m

def sub(a, b):
    """
    Compute the difference of two numbers
    I don't know the time

    >>> sub(1, 2)
    -1
    >>> sub(2, 1)
    1
    >>> sub(1, 0)
    1
    """
    return a - b


def add(a, b):
    """
    Compute the sum of two numbers
    a and b are number

    >>> add(1, 2)
    3
    >>> add(1, 0)
    1
    >>> add(-2, 1)
    -1
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
