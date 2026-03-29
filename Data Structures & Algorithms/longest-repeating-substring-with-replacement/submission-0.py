class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_table = {}

        l = 0
        result = 0
        freq = 0

        for r in range(len(s)):
            hash_table[s[r]] = hash_table.get(s[r], 0) + 1
            freq = max(freq, hash_table[s[r]])

            while (r - l + 1) - freq > k: # todo more sliding window approaches, was solved partially
                hash_table[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result

