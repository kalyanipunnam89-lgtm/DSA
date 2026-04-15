class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        v=[0]*n
        pv=[0]*n
        check=[0]*n
        def dfs(node):
            v[node]=1
            pv[node]=1
            for nei in graph[node]:
                if v[nei]==0:
                    if dfs(nei):
                        return True
                elif pv[nei]==1:
                    return True
            check[node]=1
            pv[node]=0
            return False
        for i in range(n):
            if v[i]==0:
                dfs(i)
        safe=[]
        for i in range(n):
            if check[i]==1:
                safe.append(i)
        return safe                                
        