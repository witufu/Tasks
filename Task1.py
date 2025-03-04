def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p*p, limit + 1, p):
                is_prime[i] = False

    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)

    return primes

def find_primes_in_range(start, end):

    all_primes = sieve_of_eratosthenes(end)
    return [p for p in all_primes if start <= p <= end]


try:
    start_range = int(input("Введите начало диапазона: "))
    end_range = int(input("Введите конец диапазона: "))


    prime_numbers = find_primes_in_range(start_range, end_range)


    print(prime_numbers)

except ValueError:
    print("Ошибка: Введите целые числа.")