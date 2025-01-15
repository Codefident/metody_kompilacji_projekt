def is_prime(n):
    if n <= 1:
        return False  # Liczby mniejsze lub równe 1 nie są pierwsze
    if n <= 3:
        return True  # 2 i 3 są liczbami pierwszymi
    if n % 2 == 0 or n % 3 == 0:
        return False  # Wyklucza liczby podzielne przez 2 lub 3

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Wyklucza liczby podzielne przez i lub i+2
        i += 6

    return True  # Jeśli żaden z powyższych warunków nie został spełniony, liczba jest pierwsza


# Przykłady użycia
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(23))  # True