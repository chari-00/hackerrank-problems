def a_op(x, y):
    if 1 <= x <= 100 and 1 <= y <= 100:
        print(x + y)
        print(x - y)
        print(x * y)
    else:
        print("Input out of range")
        
x = int(input())
y = int(input())
a_op(x, y)