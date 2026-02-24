class Solution:
    def countTriples(self, n: int) -> int:
        square = {i*i for i in range(1, n+1)}
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a*a + b*b in square:
                    count += 1
        return count            
        