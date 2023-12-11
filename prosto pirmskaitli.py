def is_prime(x):
    i = 0
    while i*i<x:
        if x%i==0:
            return False
        i += 1
    return True

primes = []
for i in range(2,100):
    if is_prime(i):
        primes.append(i)


s = set()
for p_1 in primes:
    for p_2 in primes:
        for p_3 in primes:
            s.add(p_1*p_2 + p_3)



res = []
u = 7
while len(res)<5:
    if u not in s:
        res.append(u)
    u += 1

print(res)