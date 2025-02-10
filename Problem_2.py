# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

class Solution:
	def pushZerosToEnd(self,arr):
		n=len(arr)
		temp_arr=[0]*n
		j=0
		for i in range(n):
			if arr[i]!=0:
				temp_arr[j]=arr[i]
				j+=1
		for i in range(n):
			arr[i]=temp_arr[i]
			return arr
sol=Solution()
print(sol.pushZerosToEnd([1,5,3,7,9,2,0]))