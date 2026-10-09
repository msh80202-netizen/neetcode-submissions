class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = sum(1 for c in Counter(s).values() if c%2 == 1)
        return odd <= 1