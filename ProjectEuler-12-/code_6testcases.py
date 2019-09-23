'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
million_primes_bool = [True]*1000000
million_primes_bool[0] = million_primes_bool[1] = False
million_primes = []

for number,isPrime in enumerate(million_primes_bool):
    if isPrime:
        for dptr in range(number*number, 1000000, number):
            million_primes_bool[dptr] = False
        million_primes.append(number)

getArithmeticSum = lambda num : ((num)*(num+1))//2

def getFactorCount(num):
    global million_primes
    ptr = 0
    summer_hummer = []
    while num != 1:
        moveOn = False
        count = 0
        while moveOn == False:
            if num % million_primes[ptr] == 0:
                num /= million_primes[ptr]
                count += 1
            else:
                moveOn = True
                summer_hummer.append(count)
        ptr += 1
    summer_hummer = [expo+1 for expo in summer_hummer]
    product = 1
    for expo in summer_hummer:
        product *= expo
    return product-1

sum_ap_cache = [0,1,3,6]
factor_count = [0,0,1,3]

times = int(input())
for _ in range(times):
    limit = int(input())
    if limit < max(factor_count):
        for ptr,factor in enumerate(factor_count):
            if limit <= factor:
                print(sum_ap_cache[ptr])
                break
    else:
        ptr = len(sum_ap_cache)
        while factor_count[-1] < limit:
            sum_ap_cache.append(getArithmeticSum(ptr))
            factor_count.append(getFactorCount(sum_ap_cache[-1]))
            ptr += 1
        print(sum_ap_cache[ptr-1])