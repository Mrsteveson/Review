heights = [1,1,4,2,1,3]

class Solution:
    def heightChecker(self, heights):
        sorts = sorted(heights)
        count = 0
        for x, y in zip(heights, sorts):
            if x != y:
                count += 1
        return count
        
s = Solution()
print(s.heightChecker(heights))