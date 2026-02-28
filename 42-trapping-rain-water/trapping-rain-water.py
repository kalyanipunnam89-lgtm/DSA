class Solution:
    def trap(self, height: List[int]) -> int:
        l = lmax = rmax = w = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                w += max(0,lmax - height[l])
                lmax = max(lmax, height[l])
                l += 1
            else:
                w += max(0,rmax - height[r])
                rmax = max(rmax,height[r])
                r -= 1
        return w

        