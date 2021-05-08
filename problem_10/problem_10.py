import math
import concurrent.futures
from functools import partial


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def calculate(_from: int, _to: int) -> int:
    total = 0
    while _from <= _to:
        if is_prime(_from):
            total += _from
        _from += 1
    return total


MAX_VALUE = 2_000_000
THREADS = 50

size = MAX_VALUE // THREADS
childrens = []


def main():
    actual = 1
    total = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in range(THREADS):
            print(f"Calculating from {actual} to {actual + size - 1}")
            childrens.append(
                executor.submit(
                    partial(calculate, _to=((actual + size) - 1)),
                    actual,
                )
            )
            actual += size

        for future in concurrent.futures.as_completed(childrens):
            total += future.result()

    print(total)


if __name__ == "__main__":
    main()