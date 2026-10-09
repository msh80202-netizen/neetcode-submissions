# Claude fixed ver

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for _ in range(k):
            best = None
            for num in count:
                if best is None or count[num] > count[best]:
                    best = num
            res.append(best)
            del count[best]   # remove it so it isn't picked again

        return res