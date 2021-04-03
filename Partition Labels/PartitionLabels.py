# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

def partitionLabels(S: str) -> list:
    end_idx = {c: i for i, c in enumerate(S)}

    start = end = 0
    result = []

    for i, c in enumerate(S):
        end = max(end, end_idx[c])
        if i == end:
            result.append(end-start+1)
            start = i+1
    return result


