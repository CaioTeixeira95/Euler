total = 1000
for a in range(1, total // 3):
    for b in range(a + 1, total // 2):
        c = total - b - a
        if (a * a) + (b * b) == (c * c):
            print(a, b, c)
            print(a + b + c)
            print(a * b * c)
print("ok")
