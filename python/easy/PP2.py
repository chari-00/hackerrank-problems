""" 
Task
Given an integer n, perform the following conditional actions:
- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird 
"""

def even_find(x):
    if x>=1 and x<=100:
        if x % 2 !=0:
            return "Weird"
        elif x % 2 == 0 and x >= 2 and x <= 5:
            return "Not Weird"
        elif x % 2 == 0 and x >= 6 and x <= 20:
            return "Weird"
        elif x % 2 == 0 and x > 20:
            return "Not Weird"
    else:
        return "Input out of range"
    
def main():
    x = int(input())
    result = even_find(x)
    print(result)
