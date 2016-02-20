#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def searchMatrix(self,matrix,target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		l=[]
		for i in range(len(matrix)):
			l.append(matrix[i][0])

		print l
		row=self.searchInsert(l,target)
		print row
		if row==-1:
			return False
		else:
			return self.binary_search(matrix[row],target)
		

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

	def searchInsert(self,nums,target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		l=0
		r=len(nums)-1
		while l<=r:
			mid=l+(r-l)/2
			if target==nums[mid]:
				return mid
			elif target<nums[mid]:
				r=mid-1
			else:
				l=mid+1

		if abs(r-l)==1:
			return max([l,r])-1
		else:
			return -1
		
def  main():
	s=Solution()
	matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
	print s.searchMatrix(matrix,10)
	

if __name__ == '__main__':
	main()