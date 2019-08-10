'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
import sys
import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

def primeFactorization(num):
    prime_factors = []
    i = 2
    while i <= num:
        if num % i == 0 and isPrime(i):
            prime_factors.append(i)
            num /= i
        else:
            i+=1
    return (prime_factors)
#MAIN
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    product = 1
    for num in range(1,n+1):
        if isPrime(num):
            product *= num
        else:
            temp = product
            factors = primeFactorization(num)
            for factor in factors:
                if temp%factor == 0:
                    temp /= factor
                else:
                    product *= factor
    print(product)
