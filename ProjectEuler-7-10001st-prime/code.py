'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
prime_occurences = [0,2,3]

def isPrime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True

t = int(input().strip())
for a0 in range(t):
    position = int(input().strip())
    try:
        if prime_occurences[position]:
            print(prime_occurences[position])
    except:
        ptr = len(prime_occurences)
        i = ptr - 1
        num = prime_occurences[i]+1
        while ptr <= position:
            if isPrime(num):
                prime_occurences.append(num)
                ptr += 1
            num += 1
        print(prime_occurences[position])
