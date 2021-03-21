# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def reverseList(list, start, end) -> list:
    if start >= end:
        return list

    list[start], list[end] = list[end], list[start]
    return reverseList(list, start+1, end-1)


