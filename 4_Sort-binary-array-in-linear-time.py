# You can also sort array using sort function as below but we have to make a function in order to sort binary array.
# arr = [ 1, 0, 1, 0, 1, 0, 0, 1]
# arr.sort()
# print(arr)


# Another method
A  = [ 1, 0, 1, 0, 1, 0, 0, 1]
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def sort(A):
 
    # count number of 0's
    zeros = A.count(0)
 
    # put 0's at the beginning
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k + 1
 
    # fill all remaining elements by 1
    for k in range(k, len(A)):
        A[k] = 1
 
if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sort(A)
 
    # print the rearranged list
    print(A)