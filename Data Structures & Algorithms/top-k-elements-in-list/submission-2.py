class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) in (0,1):
            return False

        result = []
        hash_table = {}

        set_nums = set(nums)

        for num in nums:
            if num in set_nums:
                hash_table[num] = hash_table.get(num, 0) + 1 # remember this!!
        print(hash_table.values())
        while k != 0:
            key = hash_table.pop(max(hash_table.values()), nums[0]) # we pop (the key) with max (the values)
            if key not in result:
                result.append(key)
            k -= 1

        return result

        