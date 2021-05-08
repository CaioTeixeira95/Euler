import math

# A function to print all prime factors of
# a given number n
def prime_factor(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


prime_factor(600851475143)
