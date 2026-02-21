class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict
        row = defaultdict(list)
        col = defaultdict(list)
        for x,y in buildings:
            row[y].append(x)
            col[x].append(y)
        for y in row:
            row[y].sort()
        for x in col:
            col[x].sort()
        covered = 0    
        for x, y in buildings:
            xs = row[y]
            ys = col[x]
            import bisect
            i = bisect.bisect_left(xs, x)
            j = bisect.bisect_left(ys, y) 
            if i > 0 and i < len(xs)-1 and j > 0 and j< len(ys)-1:
                covered += 1
        return covered                     
        