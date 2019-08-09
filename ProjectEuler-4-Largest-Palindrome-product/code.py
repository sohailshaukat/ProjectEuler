'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
import sys
import math

def isPalindrome(num):
    original_num = str(num)
    reversed_num = original_num[::-1]
    return original_num == reversed_num

def hasThreeDigitsFactors(num):
    factors_list = []
    for i in range(100,math.ceil(math.sqrt(num))):
        if num % i == 0:
            if len(str(i)) == 3 and len(str(int(num/i))) == 3:
                factors_list.append(i)
                factors_list.append(num/i)
    return len(factors_list)>1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for num in range(n-1,999,-1):
        if isPalindrome(num):
            if hasThreeDigitsFactors(num):
                print(num)
                break
