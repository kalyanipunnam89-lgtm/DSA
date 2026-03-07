class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        res=0
        cur_end=0
        next_end=0
        i=0
        n=len(clips)
        while cur_end<time:
            while i<n and clips[i][0]<=cur_end:
                next_end=max(next_end,clips[i][1])
                i+=1
            if next_end==cur_end:
                return -1
            res+=1
            cur_end=next_end
        return res            
        