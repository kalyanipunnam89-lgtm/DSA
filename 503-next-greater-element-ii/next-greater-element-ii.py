class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        st=[]
        for i in range(2*n):
            idx=i%n
            while st and nums[idx]>nums[st[-1]]:
                prev=st.pop()
                ans[prev]=nums[idx]
            if i<n:
                st.append(idx)
        return ans            
        