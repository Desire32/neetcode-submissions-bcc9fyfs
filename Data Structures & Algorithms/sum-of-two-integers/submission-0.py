class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b # AND (&)
            a = a ^ b # XOR (^)
            b = carry << 1 # Move
            print(f"carry, a, b: {bin(carry)[2:], bin(a)[2:] , bin(b)[2:]} ")
        return a