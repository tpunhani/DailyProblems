# returns true or false
def pallindromeCheck(list)-> bool:
    start = 0
    end = len(list)-1
    while(start < end):
        if list[start] != list[end]:
            return False
        start += 1
        end -= 1
    return True
