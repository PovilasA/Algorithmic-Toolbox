# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    importance = [float(v)/w for v, w in zip(values, weights)] 
    [(i, v, w) for (i, v, w) in sorted(zip(importance, values, weights))]
    
    
    for sorted(importance)[::-1
    from IPython import embed
    embed()
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
