# Given a unsorted integer array, find a pair with the given sum in it.
"""
Example:

Input:
 
arr = [8, 7, 2, 5, 3, 1]
sum = 10
 
Output:
 
Pair found (8, 2)
or
Pair found (7, 3)
 
 
Input:
 
arr = [5, 2, 6, 8, 1, 9]
sum = 121
 
Output: Pair not found 
"""

# arr = [8, 7, 2, 5, 3, 1]
# sum = 10
arr = [5, 2, 6, 8, 1, 9]
sum = 121

arr.sort() # sorting arr

def findPair(arr,sum):
    for i in arr:
        for j in arr:
            if i + j ==sum:
                print(f"Pair found: ({i},{j})")
                return
    print("Pair not found.")

findPair(arr,sum)