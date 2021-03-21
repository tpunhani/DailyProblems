# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def pallindromeCheck(list)-> bool:
    start = 0
    end = len(list)-1
    while(start < end):
        if list[start] != list[end]:
            return False
        start += 1
        end -= 1
    return True


# %%
pallindromeCheck("ABCBA")


# %%



