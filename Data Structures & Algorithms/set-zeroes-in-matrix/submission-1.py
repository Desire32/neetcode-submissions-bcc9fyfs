from collections import defaultdict

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        hash_table = defaultdict(set)
        for i, arr in enumerate(matrix):
            for pos, num in enumerate(arr):
                if num not in hash_table and num == 0:
                    matrix[i] = [0 for _ in matrix[i]]
                    hash_table[num].add(pos)
        
        for i in range(len(matrix)):
            for value in hash_table[0]:
                matrix[i][value] = 0
                
                            
        