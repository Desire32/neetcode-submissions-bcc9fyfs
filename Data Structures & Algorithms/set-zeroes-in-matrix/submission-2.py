# from collections import defaultdict

# class Solution: [a mess]
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         hash_table = defaultdict(set)
#         for i, arr in enumerate(matrix):
#             for pos, num in enumerate(arr):
#                 if num not in hash_table and num == 0:
#                     matrix[i] = [0 for _ in matrix[i]]
#                     hash_table[num].add(pos)
        
#         for i in range(len(matrix)):
#             for value in hash_table[0]:
#                 matrix[i][value] = 0



from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = set()
        cols_to_zero = set()
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in rows_to_zero or c in cols_to_zero:
                    matrix[r][c] = 0
                            
        