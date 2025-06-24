
"""
Task
Given the participants' score sheet for your University Sports Day, you are tasked with finding the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
"""

def runnerup(arr):
    arr = [int(x) for x in arr] 
    arr = list(set(arr))        
    arr.sort(reverse=True)       
    return arr[1]                

n = int(input())
arr = input().split()
print(runnerup(arr))
