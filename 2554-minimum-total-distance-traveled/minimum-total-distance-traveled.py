class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        @lru_cache(None)
        def dfs(i,j):
            if i == len(robot):
                return 0
            if j == len(factory):
                return math.inf
            res = dfs(i,j+1)
            dist=0
            for k in range(factory[j][1]):
                if i+k >= len(robot):
                    break
                dist += abs(robot[i+k] - factory[j][0])
                res=min(res,dist+dfs(i+k+1,j+1))
            return res
        return dfs(0, 0)                        