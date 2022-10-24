#function takes a number and returns true or false determining if prime
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

        
def print_factors(n: int) -> None:
    print(n, "->", factors(n))



print(is_prime(13))





    
    
