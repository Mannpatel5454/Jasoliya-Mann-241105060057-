for i in range(2, 31):
    is_prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

print()