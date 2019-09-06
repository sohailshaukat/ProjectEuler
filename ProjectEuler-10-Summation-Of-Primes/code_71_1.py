'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def isPrime(num):
    if num == 1:
        return False
    else:
        i = 2
        while i <= int(num**0.5)+1:
            if num%i == 0 and i != num:
                return False
            i += 1
    return True

dp = [2,3,5,7,11,13,17,19]

times = int(input())

for _ in range(times):
    sum_of_primes = 0
    limit = int(input())
    if limit <= dp [-1]:
        ptr = 0
        while dp[ptr] <= limit:
            sum_of_primes += dp[ptr]
            ptr += 1
    else:
        sum_of_primes = sum(dp)
        number = dp[-1]+2
        while number <= limit:
            if isPrime(number):
                dp.append(number)
                sum_of_primes += number
            number += 2
    print(sum_of_primes)
