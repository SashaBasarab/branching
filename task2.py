def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sequence = [29, 15, 17, 21, 23, 12, 31, 37, 19, 4, 8, 9, 3, 11, 13, 27, 33, 2, 5, 7]

prime_count = sum(1 for num in sequence if is_prime(num))

print(f"Кількість простих чисел у послідовності: {prime_count}")
