class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        secret=set([0,firstPerson])
        i = 0
        while i < len(meetings):
            time=meetings[i][2]
            graph=defaultdict(list)
            people=set()
            while i<len(meetings) and meetings[i][2 ]==time:
                x,y,_=meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1
            queue = deque()
            visited = set()
            for p in people:
                if p in secret:
                    queue.append(p)
                    visited.add(p)
            while queue:
                u=queue.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            secret.update(visited)
        return list(secret)                            
        