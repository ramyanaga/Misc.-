import time

def calculate_primes_old(limit):
    primes = []
    for i in xrange(2, limit):
        count = 0
        for j in xrange(2, i):
            if i % j == 0:
                count += 1
        if count == 1:
            primes.append(primes)
    return primes

def calculate_primes(limit):
    primes = []
    for i in xrange(2, limit):
        count = 0
        for j in xrange(2, i):
            if i % j == 0:
                count += 1
            if count == 1:
                break
        if count == 0:
            primes.append(i)
    return primes

def calculate_primes_new(limit):
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

if __name__=='__main__':
    for num in range(1000, 10001, 1000):
        start = time.time()
        calculate_primes_old(num)
        print '[OLD: %d] Elapsed time: %f' % (num, time.time() - start)

    for num in range(1000, 10001, 1000):
        start = time.time()
        calculate_primes(num)
        print '[MEH: %d] Elapsed time: %f' % (num, time.time() - start)

    for num in range(1000, 10001, 1000):
        start = time.time()
        calculate_primes_new(num)
        print '[NEW: %d] Elapsed time: %f' % (num, time.time() - start)


