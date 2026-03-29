class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [n for n in range(0, n+1)]
        count = 0
        for i, num in enumerate(output):
            while num >=1: 
                num &= (num-1)
                count+=1
            output[i] = count
            count = 0
        return output

    