s = sum(range(1, 101)) ** 2
ss = sum(list(map(lambda x: x ** 2, range(1, 101))))

print(s - ss)
