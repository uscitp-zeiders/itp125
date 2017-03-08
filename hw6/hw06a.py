import math
val = 0
primes = [2,3]
def isPrime(num):
    for i in primes:
        if num % i == 0:
            return False
    return True

for i in xrange(2,100000):
    if isPrime(i):
        primes.append(i)
print primes
for i in primes:
    if 600851475143 % i == 0:
        val = i
start = 600851475143
i = 0
factors = []
while i < len(primes):
    if(start%primes[i] == 0):
        start = start/primes[i]
        factors.append(primes[i])
    else:
        i = i +1
print(max(factors))