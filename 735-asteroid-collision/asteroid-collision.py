class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for ast in asteroids:
            while st and ast<0 and st[-1]>0:
                if st[-1]<-ast:
                    st.pop()
                    continue
                elif st[-1]==-ast:
                        st.pop()
                break
            else:
                st.append(ast)
        return st                
        