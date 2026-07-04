class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)
        l=[]
        for i in range(len(points)-1):
            l.append(points[i][0]-points[i+1][0])
        return max(l)    