from collections import deque # 0(1) access instead of list.pop(n) -> 0(n)

# BFS, Kann Algorithm approach
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. create a dictionary of alien letters
        alien_dict = set()
        for word in words:
            for ch in word:
                alien_dict.add(ch)

        # 2. assuming each node has in_degree == 0 
        in_degree = {ch: 0 for ch in alien_dict}
        
        # 3. adj connections between nodes
        adj = {ch: [] for ch in alien_dict}

        # 4. comparing two words between each other (if A < B && B < C, then A < C)
        for i in range(0, len(words) - 1):
            wrd1, wrd2 = words[i], words[i+1]
            L = min(len(wrd1), len(wrd2)) # solving the edges problem, comparing words when one is part of another
            for j in range(L):
                if wrd1[j] != wrd2[j]:  # wrd1 comes in alphabet sooner than wrd2
                    ch1, ch2 = wrd1[j], wrd2[j]
                    print(f"char1, char2: {ch1, ch2}")
                    if ch2 not in adj[ch1]:
                        adj[ch1].append(ch2)
                        in_degree[ch2] += 1
                        print(f"in-degree: {in_degree[ch2]}")
                    break

                else: # edge case, one word is the prefix of another, ex. ("apple", "app")
                    if len(wrd1) > len(wrd2):
                        return ""
        # 5. BFS part, place letters that don't have any other letters after them
        q = deque([ch for ch in in_degree if in_degree[ch] == 0])
        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for njb in adj[ch]:
                in_degree[njb] -= 1

                if in_degree[njb] == 0:
                    q.append(njb)
        
        if len(res) < len(in_degree):
            return ""

        return "".join(res)





