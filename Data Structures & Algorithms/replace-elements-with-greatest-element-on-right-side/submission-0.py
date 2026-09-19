class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       #Initialize the maximum on the right 
        max_right = -1
        #loop from right to left 
        for i in range(len(arr) - 1, -1, -1):
            #replace the current element and update the maximum 
            arr[i], max_right = max_right, max(max_right, arr[i])
        return arr
