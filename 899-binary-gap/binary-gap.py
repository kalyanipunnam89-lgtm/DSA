class Solution:
    def binaryGap(self, n: int) -> int:
        b=bin(n)[2:]
        prev=-1
        ans=0
        for i in range(len(b)):
            if b[i] == '1':
                if prev!=-1:
                    ans=max(ans,i-prev)
                prev=i
        return ans            

        