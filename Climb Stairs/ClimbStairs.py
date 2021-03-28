# Find the no. of ways a person can climb n stairs if he is only allowed to take either 1 step at a time or 2 steps at a time.
def climbStairs(n: int) -> int:
    if n==1:
        return 1

# no of ways for 0th stair
    first = 1

# no of ways for 1st stair
    second = 1

# apply bottom up approach to find ways for 2nd step, 3rd step and so on
    for i in range(2,n+1):
        third = first+second
        first = second
        second = third

    return second


