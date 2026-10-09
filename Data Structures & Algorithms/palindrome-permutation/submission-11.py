# First attempt
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        onlyValue = list(count.values())

        even = {"e": 0, "o": 0}

        for value in onlyValue:
            if value%2 == 0:
                even["e"] += 1
            else:
                even["o"] += 1
        
        if even["o"] == 0 or even["o"] == 1:
            return True
        else:
            return False