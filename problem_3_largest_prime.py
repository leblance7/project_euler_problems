def is_factor(n: int, x: int) -> bool:
    return n % x == 0


def factors(n: int) -> list[int]:
    results = []
    for x in range(2, n):
        if is_factor(n,x):
            results.append(x)
    return results


def is_prime(n: int) -> bool:
    if factors(n) == []:
        return True
    else:
        return False

#Takes a list of factors and determines the prime factors

def prime_factors(n: int) -> list:
    facts = factors(n)
    prime_factors =[]
    for x in facts:
        if is_prime(x) == True:
            prime_factors.append(x)
    return prime_factors
        
def print_factors(n: int) -> None:
    print(n, "->", prime_factors(n))


print_factors(13195)

