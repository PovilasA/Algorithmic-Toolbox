# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    
def gcd(a, b):
    if a == b: return a
    if a == 0 or b == 0: return max(a, b)
    
    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)
        

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
