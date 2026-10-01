class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            current = arr[i]
            arr[i] = right_max
            right_max = max(current, right_max)
        return arr
        