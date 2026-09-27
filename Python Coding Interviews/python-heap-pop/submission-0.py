import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    i = len(heap)
    popped = []
    while i > 0:
        popped.append(heapq.heappop(heap))
        i -= 1
    return popped

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
