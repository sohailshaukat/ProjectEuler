'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
import sys
fib_arr = [0,1,2]
l = 3
def fib(n):
    global fib_arr
    global l
    if l > n+1:
        return fib_arr[n+1]
    else:
        result = fib(n-1)+fib(n-2)
        fib_arr.insert(n+1 , result)
        l+=1
        return result

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    result = 0
    next_value = 0
    while next_value < n:
        result += fib(i)
        i+=3
        next_value = fib(i)
    print(result)
