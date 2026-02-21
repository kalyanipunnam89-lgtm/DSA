class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        g=[]
        c=1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c+=1
            else:
                g.append(c)
                c=1
        g.append(c)
        ans=0
        for i in range(1,len(g)):
            ans+=min(g[i-1],g[i])
        return ans                        