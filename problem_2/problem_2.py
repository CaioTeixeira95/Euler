a, b = 1, 2
result = 0
while True:
    a, b = b, a + b
    if a >= 4_000_000:
        break
    if a % 2 == 0:
        result += a

print(result)
