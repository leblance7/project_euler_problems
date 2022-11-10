import sys


class IntRef:
    def __init__(self, value):
        self.value = value

    def iadd(self, n):
        self.value += n

    def __str__(self):
        return str(self.value)

WORK = IntRef(0)

def is_factor(n: int, x:int) -> bool:
    result = n % x == 0
    print(f"is_factor({n}, {x}) -> {result}")
    return result
    #return n % x == 0



def factors(n: int) -> list[int]:
    #print(f"factors({n}) ...")
    results = []
    if n == 2:
        return []
    if n % 2 == 0:
        results.append(2)
    for x in range(3, n//2+1, 2):
        #increment work to measure loop efficenty
        WORK.iadd(1)
        #print(f" ... factors({n}) for x={x}") 
        if is_factor(n ,x):
            results.append(x)
    print(f"factors({n}) -> {results}")
    return results


def is_prime(n: int) -> bool:
    #print(f"is_prime({n})...")
    res = factors(n)
    if res == []:
        print(f"is_prime({n}) -> True")
        return True
    else:
        print(f"is_prime({n}) -> False")
        return False

#Takes a list of factors and determines the prime factors

def prime_factors(n: int) -> list:
    print(f"prime_factors({n})...")
    facts = factors(n)
    prime_facts =[]
    for x in facts:
        #print(f" ... prime_factors({n}) for x={x}")
        if is_prime(x) == True:
            prime_facts.append(x)
    return prime_facts
    
        
def print_factors(n: int) -> None:
    print(n, "->", prime_factors(n))


#print_factors(13195)
print_factors(int(sys.argv[1]))
#print_factors(600851475143)
print(f"WORK {WORK}")
