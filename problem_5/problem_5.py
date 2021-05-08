num = 2525
while True:
    found = True
    for i in range(1, 21):
        if num % i != 0:
            found = False
            break

    if found:
        print(num)
        break
    num += 5
