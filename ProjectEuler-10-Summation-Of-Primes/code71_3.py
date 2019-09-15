'''
problem URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def depleter(num_line , prime_ptr):
    prime = num_line[prime_ptr]
    ptr = prime_ptr + 1
    while ptr < len(num_line):
        if num_line[ptr] % prime == 0:
            del num_line[ptr]
        ptr += 1
    return num_line

times = int(input())

dynamic_number_line = [2,3,5,7] 

for _ in range(times):
    num = int(input())
    number_line = []
    if num <= dynamic_number_line[-1]:
        summer = 0
        for ptr,number in enumerate(dynamic_number_line):
            if number > num:
                break
            summer += number
        print(summer)
    else:
        number_line = dynamic_number_line + list(range(dynamic_number_line[-1]+1, num +1))
        ptr = 0
        while number_line[ptr] <= (num**0.5):
            number_line = depleter(number_line, ptr)
            ptr += 1
        dynamic_number_line = number_line
        print(sum(number_line))
        