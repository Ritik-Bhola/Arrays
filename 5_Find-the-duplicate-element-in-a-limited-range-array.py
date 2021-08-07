"""
Input:  { 1, 2, 3, 4, 4 }
Output: The duplicate element is 4
"""

# Function to find a duplicate element in a limited range list
def findDuplicate(A):
 
    # create a visited list of size `n+1`
    # we can also use a dictionary instead of a visited list
    visited = [False] * (len(A) + 1)
 
    # for each element in the list, mark it as visited and
    # return it if seen before
    for i in range(len(A)):
 
        # if the element is seen before
        if visited[A[i]]:
            return A[i]
 
        # mark element as visited
        visited[A[i]] = True
 
    # no duplicate found
    return -1
 
 
if __name__ == '__main__':
 
    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(A)`
    A = [1, 2, 3, 4, 4]
 
    print("The duplicate element is", findDuplicate(A))