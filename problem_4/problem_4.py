palindromes = []
for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        res = str(j * i)
        if res == res[::-1]:
            palindromes.append(int(res))

print(max(palindromes))
