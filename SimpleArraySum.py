def SimpleArraySum(nums : List[int]) -> int:
    """
    >>> sol_one = SimpleArraySum([1, 2, 3, 4, 10, 11])
    >>> print(sol_one)
    31

    >>> sol_two = SimpleArraySum([1, 2, 3])
    >>> print(sol_two)
    6
    """
    return sum(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod()