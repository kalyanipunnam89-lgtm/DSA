class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        cs=""
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                st.append((num,cs))
                num=0
                cs=""
            elif ch==']':
                k,prev=st.pop()
                cs=prev+k*cs
            else:
                cs+=ch
        return cs                

        