'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
numbers = [True] * 1000000
numbers[0] = numbers[1] = False
sums = [0] * 1000000

for number,isPrime in enumerate(numbers):
    if isPrime:
        for dptr in range(number*number, 1000000, number):
            numbers[dptr] = False
        sums[number] = sums[number-1]+number
    else:
        sums[number] = sums[number - 1]

times = int(input())
for _ in range(times):
   limit = int(input())
   print(sums[limit])
