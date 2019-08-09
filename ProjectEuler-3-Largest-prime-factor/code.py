'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
import sys
import math

def checkPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True

t = int(input())
for a0 in range(t):
    n = int(input())
    factor_list = []
    factor_list_asc = []
    factor_list_dsc = []
    for num in range(1,int(math.sqrt(n))+1):
        if n%num==0:
            factor_list_asc.append(num)
            factor_list_dsc.append(int(n/num))
    factor_list = factor_list_asc + factor_list_dsc[::-1]
    prime_factors = [el for el in factor_list if checkPrime(el)]
    print(prime_factors[-1])
