class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n=len(events)
        max_value_from=[0] * n
        max_value_from[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            max_value_from[i] = max(max_value_from[i+1],events[i][2])
        starts = [e[0] for e in events]
        ans = 0
        for i, (s, e, v) in enumerate(events):
            idx = bisect_right(starts, e)
            if idx < n:
                ans = max(ans, v + max_value_from[idx])
            ans = max(ans, v)
        return ans               