class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            ans[i] = num
        return ans + ans