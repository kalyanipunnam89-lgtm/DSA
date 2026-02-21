class Solution:
    def checkValidString(self, s: str) -> bool:
        minopen,maxopen=0,0
        for ch in s:
            if ch=='(':
                minopen+=1
                maxopen+=1
            elif ch==')':
                minopen-=1
                maxopen-=1    
            elif ch=="*":
                minopen-=1
                maxopen+=1
            if maxopen<0:
                return False
            if minopen<0:
                minopen=0
        return minopen==0            


        