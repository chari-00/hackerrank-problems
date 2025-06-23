
"""
Task
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following: 123...n
Note that "..." represents the consecutive values in between.
"""
def loop(n):
    i = 1;
    while i<=n:
        print(i, end='')
        i += 1
        
n = int(input())
loop(n)