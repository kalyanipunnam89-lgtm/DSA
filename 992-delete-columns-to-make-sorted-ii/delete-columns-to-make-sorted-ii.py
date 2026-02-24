class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        deleted=0
        sorted_pairs=[False]*(n-1)
        for col in range(m):
            bad=False
            for i in range(n-1):
                if not sorted_pairs[i] and strs[i][col]>strs[i+1][col]:
                    bad=True
                    break
            if bad:
                deleted += 1
                continue
            for i in range(n-1):
                if strs[i][col]<strs[i+1][col]:
                    sorted_pairs[i]=True
        return deleted                        
        