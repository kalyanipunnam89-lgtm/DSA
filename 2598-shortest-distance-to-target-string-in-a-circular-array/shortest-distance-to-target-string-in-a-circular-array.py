class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        min_dist=float('inf')
        for i in range(n):
            if words[i]==target:
                dist=abs(i-startIndex)
                circular_dist=n - dist
                min_dist = min(min_dist,min(dist, circular_dist))
        return min_dist if min_dist != float('inf') else -1

 