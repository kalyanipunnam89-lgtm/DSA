class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        n=len(heights)
        ma=0
        i=0
        while i<n:
            h=heights[i]
            start=i
            while st and st[-1][1]>h:
                idx,height=st.pop()
                ma=max(ma,height*(i-idx))
                start=idx
            st.append((start,h))
            i+=1
        for idx,height in st:
            ma=max(ma,height*(n-idx))
        return ma            