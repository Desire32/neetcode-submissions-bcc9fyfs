class Solution:
    def reverseBits(self, n: int) -> int:
        n = f"{n:032b}"
        rev = ''.join(reversed(str(n)))
        return int(rev, 2)