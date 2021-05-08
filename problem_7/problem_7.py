import math


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


count = 6
num = 15
while True:
    if is_prime(num):
        count += 1
        if count == 10001:
            print(num)
            break
    num += 2
