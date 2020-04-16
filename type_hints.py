#!/usr/bin/env python
import typing as T

Numeric = T.Union[int, float]
#  T.Any T.Iterable T.List[type]  T.Tuple[Type]
#   def name(...) -> return_type:

def c2f(celsius: Numeric) -> float:
    fahrenheit = ((9 * celsius) / 5) + 32
    return fahrenheit


f = c2f(37.1)
print(f)

f = c2f(37)
print(f)

# type hinting vs type checking
# type hinting? YES
# type checking? NO


def get_powers(n: int) -> T.Iterable:
    return n, n ** 2, n ** 3


x = get_powers(5)
print(x)

def doit(num_list: T.Iterable[Numeric]) -> T.List[float]:
    return [10]

doit([5])


