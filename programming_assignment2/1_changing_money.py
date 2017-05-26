# Uses python3
import sys

def get_change(m):
    banknotes = [10, 5, 1] # decreasing order
    m = int(m)
    n = 0
    for b in banknotes:
        n = n + m//b
        m = m - m//b * b
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
