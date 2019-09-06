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

dp = [2,3,5,7,11,13]
sp = [2,5,10,17,28,41]
times = int(input())

for _ in range(times):
    limit = int(input())
    if limit <= dp[-1]:
        ptr = 0
        while dp[ptr+1] <= limit:
            ptr += 1
            if ptr == len(dp)-1:
                break
        print(sp[ptr])
    else:
        number = dp[-1]+2
        while number <= limit:
            if isPrime(number):
                dp.append(number)
                sp.append(number + sp[-1])
            number += 2
        print(sp[-1])
