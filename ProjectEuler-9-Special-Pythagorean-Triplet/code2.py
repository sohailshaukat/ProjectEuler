'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
times = int(input())
for _ in range(times):
    num = int(input())
    maximum_product = -1
    for a in range(1,(num//3)+1):
        b = (((num**2)/2) - (num*a)) // (num - a)
        if b > 0:
            hyp = (a**2 + b**2)**0.5
            if a + b + hyp == num:
                prod = a*b*hyp
                if maximum_product < prod:
                    maximum_product = prod
    print(int(maximum_product))
