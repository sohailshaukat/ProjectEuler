'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
import sys,math

def arithmetic_sum(d,n):
    a=d
    return (n)*(2*(a) + (n-1)*d)
def summer(a,b,c):
    ax = a + b -c
    x = (ax>>1)
    return x

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n-1
    t_3 = n//3
    t_5 = n//5
    t_15 = n//15
    sum_3 = (arithmetic_sum(3, t_3))
    sum_5 = (arithmetic_sum(5, t_5))
    sum_15 = (arithmetic_sum(15, t_15))
    result = summer(sum_3, sum_5, sum_15)
    print(result)
