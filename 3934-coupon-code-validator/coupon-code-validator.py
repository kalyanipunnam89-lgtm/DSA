class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics":0,"grocery":1,"pharmacy":2,"restaurant":3
        }
        valid = []
        for c,b,active in zip(code,businessLine,isActive):
            if not active:
                continue
            if not c or any(not(ch.isalnum() or ch=='_') for ch in c):
                continue
            if b not in order:
                continue
            valid.append((order[b],c))
        valid.sort(key=lambda x:(x[0],x[1]))
        return [code for _,code in valid]                
        