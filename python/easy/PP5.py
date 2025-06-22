
"""
Task
The provided code stub reads an integer, , from STDIN. For all non-negative integers i<n, print i^2. 
"""

def sq(x):
    if 1 <= x <= 20:
        for i in range(0, x):
            print(i * i)
    else:
        return "Input out of range"

x = int(input())
result = sq(x)
if result is not None:
    print(result)