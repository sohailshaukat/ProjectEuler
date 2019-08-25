'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3

def product(numbers):
    prod = 1
    if '0' in numbers:
        return 0
    else:
        for number in numbers:
            prod *= int(number)
        return prod

times = int(input())
for _ in range(times):
    inp = input().split()
    num_len = int(inp[0])
    bracket_length = int(inp[1])
    num = list(input())
    front_head = bracket_length
    back_tail = 0
    maximum_prod = 0
    prod = 0
    while front_head < num_len:
        prod = product(num[back_tail:front_head])
        if prod > maximum_prod:
            maximum_prod = prod
        front_head += 1
        back_tail += 1
    print(maximum_prod)
