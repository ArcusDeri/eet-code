# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
def merge(arr, left, middle, right, tempArr):
    leftPtr = left
    rightPtr = middle + 1
    resPtr = left
    for i in range(left, middle + 1):
        tempArr[i] = arr[i]
    for i in range(middle + 1, right + 1):
        tempArr[i] = arr[i]

    while leftPtr <= middle and rightPtr <= right:
        if (tempArr[leftPtr] < tempArr[rightPtr]):
            arr[resPtr] = tempArr[leftPtr]
            leftPtr += 1
        else:
            arr[resPtr] = tempArr[rightPtr]
            rightPtr += 1
        resPtr += 1
    
    while leftPtr <= middle:
        arr[resPtr] = tempArr[leftPtr]
        resPtr += 1
        leftPtr += 1

    while rightPtr <= right:
        arr[resPtr] = tempArr[rightPtr]
        resPtr += 1
        rightPtr += 1
    

# Thread temp array all the way down. This way only one array is created.
# Alternatively tempArr could be ommited and created as needed in `merge`
# but then numerous creations would occur which isn't effective.
def innerMergeSort(arr, left, right, tempArr):
    if left >= right:
        return

    middle = (left + right) // 2
    innerMergeSort(arr, left, middle, tempArr)
    innerMergeSort(arr, middle + 1, right, tempArr)
    merge(arr, left, middle, right, tempArr)

def mergeSort(arr):
    innerMergeSort(arr, 0, len(arr) - 1, [0] * len(arr))

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted = heights[:]
        mergeSort(sorted)
        k = 0
        for i in range(len(heights)):
            if heights[i] != sorted[i]:
                k += 1
        
        return k

