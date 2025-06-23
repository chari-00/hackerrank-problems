
"""
Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note: that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
 """

def is_leap(x):
    if x % 4 ==0 and (x % 100 != 0 or x % 400 == 0):
        return True
    else:
        return False
    
x = int(input())
print(is_leap(x))