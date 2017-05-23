# Uses python3
def calc_fib(n):
    if n == 0: return 0
    F = [0,1]
    m = 2
    while (m <= n):
        F.append(F[m-2] + F[m-1])
        m = m+1
    return F[len(F)-1]

n = int(input())
print(calc_fib(n))
