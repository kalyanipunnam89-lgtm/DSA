class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = []
                # collect k*k elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        nums.append(grid[x][y])
                nums.sort()
                min_diff = float('inf')
                # check adjacent differences
                for p in range(1, len(nums)):
                    if nums[p] != nums[p - 1]:
                        min_diff = min(min_diff, nums[p] - nums[p - 1])
                # if all elements same
                ans[i][j] = 0 if min_diff == float('inf') else min_diff
        return ans
        