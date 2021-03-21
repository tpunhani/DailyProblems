
# reverse the list recursively
def reverseListRecursive(list, start, end) -> list:
    if start >= end:
        return list

    list[start], list[end] = list[end], list[start]
    return reverseListRecursive(list, start+1, end-1)


# In place iterative solution with two pointers
def reverseListIterative(list) -> list:
    i=0
    j=len(list)-1

    while i < j:
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1
    return list



