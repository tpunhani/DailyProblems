# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


def topKFrequent(nums, k: int):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
                
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        res = []
        for k, v in freq[:k]:
            res.append(k)
            
        return res





