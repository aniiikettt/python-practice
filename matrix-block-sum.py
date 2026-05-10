class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]
