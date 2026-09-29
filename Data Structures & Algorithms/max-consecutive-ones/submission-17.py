from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                best = max (best, current)
            else:
                current = 0

        return best

nums = [1, 1, 0, 1, 1, 1]
print(Solution().findMaxConsecutiveOnes(nums))