# Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].

def countBits(self, num: int) -> List[int]:
        result = []
        result.append(0)
        
        for i in range(1, num+1):
            result.append(result[int(i/2)] + i%2)
            
        return result


