import math
from functools import reduce


def triangle_number(before: int, n: int) -> int:
    return before + n


def factors(n: int) -> int:
    step = 2 if n % 2 else 1
    return len(
        set(
            reduce(
                list.__add__,
                (
                    [i, n // i]
                    for i in range(1, int(math.sqrt(n)) + 1, step)
                    if n % i == 0
                ),
            )
        )
    )


n = 1
before = 0
while True:
    tn = triangle_number(before, n)
    print(tn)
    if factors(tn) > 500:
        print("Result:", tn)
        break
    before = tn
    n += 1