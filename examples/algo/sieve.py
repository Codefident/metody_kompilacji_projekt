def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    is_prime = []
    for i in range(n + 1):
        is_prime.append(True)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    return primes


n = 100
print(sieve_of_eratosthenes(n))
