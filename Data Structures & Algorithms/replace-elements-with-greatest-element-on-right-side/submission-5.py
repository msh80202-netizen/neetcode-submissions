class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse itertaion
        # new max = max(oldmax, arr[i])

        rightMax = -1

        #start from the very last element of the array, iterate reverse, stop when reached the first element
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
