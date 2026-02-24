class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        delete_count=0
        for c in range(cols):
            for r in range(1,rows):
                if strs[r][c]<strs[r-1][c]:
                    delete_count+=1
                    break
        return delete_count            
        