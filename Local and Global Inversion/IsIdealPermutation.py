# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

# Return true if and only if the number of global inversions is equal to the number of local inversions.

def isIdealPermutation(self, A: List[int]) -> bool:
    maximum = -1
    for i in range(0, len(A)-2):
        maximum = max(A[i], maximum)
        if i+2 <= len(A) and maximum > A[i+2]:
            return False
            
    return True


