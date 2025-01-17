# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

class Solution:
    def getSecondLargest(self, arr):
        first=arr[0]
        second=-1
        for i in range(len(arr)):
            if arr[i]>first:
                second=first
                first=arr[i]
            elif second<arr[i]<first:
                second=arr[i]
        
        return second
sol=Solution()
print(sol.getSecondLargest([1,5,3,7,9,2,0]))