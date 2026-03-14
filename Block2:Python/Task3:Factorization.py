def prime_factors(n: int) -> list:

    if n < 2:
        return []
    
    factors = []
    divisor = 2
    
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2
    
    if n > 1:
        factors.append(n)
    
    return factors

n = 56
print(prime_factors(n))

print(prime_factors(12))
print(prime_factors(13))
print(prime_factors(100))
print(prime_factors(1))