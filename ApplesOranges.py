from typing import List

def Solution(s : int, t : int, a : int, b : int, apples : List[int], oranges : List[int]) -> Tuple[int]:
    """_summary_

    >>> sol_one = Solution(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
    >>> print(sol_one)
    (1, 2)

    >>> sol_two = Solution(7, 11, 5, 15, [-2, 2, 1], [5, -6])
    >>> print(sol_two)
    (1, 1)
    """
    apple = [i for i in [apple + a for apple in apples] if i in range(s, t+1)]
    orange = [i for i in [orange + b for orange in oranges] if i in range(s, t+1)]
    return len(apple), len(orange)

if __name__ == '__main__':
    import doctest
    doctest.testmod()