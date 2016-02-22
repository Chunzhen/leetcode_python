#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def searchMatrix(self,matrix,target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		l=len(matrix[0])-1
		for i in range(len(matrix)):
			if matrix[i][0]<=target and matrix[i][l]>=target:
				b=self.binary_search(matrix[i],target)
				if b:
					return True

		return False
		

	def binary_search(self,nums,target):
		l=0
		r=len(nums)-1
		while l<=r:
			mid=l+(r-l)/2
			if target<nums[mid]:
				r=mid-1
			elif target>nums[mid]:
				l=mid+1
			else:
				return True

		return False

		
def  main():
	s=Solution()
	#matrix=[[1,4,7,11],[2,5,8,12],[3,6,9,16,22],[10,13,14,17,24]]
	matrix=[[12]]
	print s.searchMatrix(matrix,12)
	

if __name__ == '__main__':
	main()