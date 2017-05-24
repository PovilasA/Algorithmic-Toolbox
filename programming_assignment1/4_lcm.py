# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
    
def gcd(a, b):
    if a == b: return a
    if a == 0 or b == 0: return max(a, b)
    
    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)
    
    
def lcm(a, b):
    if a > b:
        A, B = a, b
    else:
        A, B = b, a
    return int(A/gcd(a, b)*B)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

