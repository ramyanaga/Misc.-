
"""def calculate_primes_new(limit):
    return_sum = 0
    primes = range(2, limit+1)
    return_primes = []
    while len(primes) > 0:
        num = primes[0]
        new_primes = []
        for i in primes:
            if i % num != 0:
                new_primes.append(i)
        primes = new_primes
        return_primes.append(num)
    return return_primes
    for num in return_primes:
        return_sum+= num 
    print return_sum

if __name__ == '__main__':
    calculate_primes_new(1000)
"""
return_sum = 0
limit = 2000000
return_sum = 0
primes = range(2, limit)
return_primes = []
while len(primes) > 0:
    num = primes[0]
    new_primes = []
    for i in primes:
        if i % num != 0:
            new_primes.append(i)
    primes = new_primes
    return_primes.append(num)
#return return_primes
for num in return_primes:
    return_sum+= num 
print return_sum
