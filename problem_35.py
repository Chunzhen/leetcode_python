#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
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

		print l,' ',r
		if abs(r-l)==1:
			return max([l,r])
		else:
			return -1


		



def  main():
	s=Solution()

	nums=[1,3,5,6]
	print s.searchInsert(nums,0)
	

if __name__ == '__main__':
	main()