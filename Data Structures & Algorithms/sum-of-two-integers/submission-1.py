class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask
        mask = 0xffffffff # interesting
        MAX_POS = 0x7FFFFFFF # maximum positive 32 bit integer
        while b != 0:
            carry = (a & b) & mask # AND (&)
            a = (a ^ b) & mask # XOR (^)
            b = (carry << 1) & mask # Move
            print(f"carry, a, b: {bin(carry)[2:], bin(a)[2:] , bin(b)[2:]} ")
        if a > MAX_POS:
            return ~(a ^ mask)
        return a