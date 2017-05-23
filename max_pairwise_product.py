# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

# from IPython import embed
# embed()

max_index1 = 0 
for i in range(1, n):
    if a[i] > a[max_index1]:
        max_index1 = i
        
max_index2 = False
for i in range(0, n):
    value = a[max_index2] if max_index2 else -1
    if i != max_index1 and a[i] > value:
        max_index2 = i

result = a[max_index1] * a[max_index2]
print(result)
