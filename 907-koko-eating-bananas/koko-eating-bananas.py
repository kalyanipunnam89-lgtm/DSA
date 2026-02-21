class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        ans=right
        while left<=right:
            mid=(left+right)//2
            hour=0
            for p in piles:
                hour+=math.ceil(p/mid)
            if hour<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans                
        