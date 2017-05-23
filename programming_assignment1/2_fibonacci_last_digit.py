# Uses python3

import fibonacci
    
def fib_last_digit(n):
    return fibonacci.calc_fib(n % 60) % 10
            

n = int(input())
print(fib_last_digit(n))





