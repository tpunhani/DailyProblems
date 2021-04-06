# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

def minOperations(self, n: int) -> int:
    target = 0
    arr = []
    for i in range(n):
        num = (2*i)+1
        arr.append(num)
        target += num
    target = target/n    
    i = 0
    j = n-1
    op = 0
    while i < j:
        if target - arr[i] > 0:
            op += target-arr[i]
        i += 1
        j -= 1
            
    return int(op)


