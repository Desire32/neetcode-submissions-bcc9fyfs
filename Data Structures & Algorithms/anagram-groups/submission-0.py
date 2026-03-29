class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        output = []
        for word in strs:
            key = ''.join(sorted(word))
            if key not in ht:
                ht[key] = []
            ht[key].append(word)
        for k,v in ht.items():
            output.append(v)
        return output