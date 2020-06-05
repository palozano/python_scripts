"""Code from book Classic
Computer Science w Python
"""


def fib1(n: int) -> int:
    return fib1(n - 2) + fib1(n - 1)
# infinite recursion, never stops


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)
# inefficient, too many calls to the function


from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # base case

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]
# efficient, manual memoization


from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)
# the decorator caches function calls so it's faster


def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
# iterative and efficient


from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = last, last + next 
        yield next


if __name__ == "__main__":
    # print(fib1(5))

    # print(fib2(5))
    # print(fib2(10))

    # print(fib3(50))

    # print(fib4(5))
    # print(fib4(10))

    # print(fib5(50))

    for i in fib6(50):
        print(i)
