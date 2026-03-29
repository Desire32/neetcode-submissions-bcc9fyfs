class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) in (0,1):
            return nums

        result = []
        hash_table = {}

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1 # remember this!!

        print(hash_table.values())
        while k != 0:
            key = max(hash_table, key=hash_table.get) # we pop (the key) with max (the values), key function to memorize
            result.append(key)
            hash_table.pop(key)
            k -= 1

        return result

        