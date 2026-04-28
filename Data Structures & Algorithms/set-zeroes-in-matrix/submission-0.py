class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        hash_table = {}
        for i, arr in enumerate(matrix):
            for pos, num in enumerate(arr):
                if num == 0:
                    matrix[i] = [0 for _ in matrix[i]]
                    hash_table[num] = pos
        
        for i in range(len(matrix)):
            matrix[i][hash_table.get(0)] = 0
                
                            
        