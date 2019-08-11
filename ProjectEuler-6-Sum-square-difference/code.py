'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=false
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    square_of_sum = ((n * (n+1))// 2) ** 2
    sum_of_squares = (((n) * (n+1) * (2*n+1)) // 6)
    print(square_of_sum-sum_of_squares)
