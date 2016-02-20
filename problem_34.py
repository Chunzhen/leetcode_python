#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def searchRange(self,nums,target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		l=self.lower_bound(nums,0,len(nums)-1,target)
		if l==-1:
			return [-1,-1]
		r=self.upper_bound(nums,l,len(nums)-1,target)
		return [l,r]

	def lower_bound(self,nums,l,r,target):
		while l<r:
			mid=(l+r)>>1 #!!!最重要,当l+r是奇数时，mid离l更近
			if target<nums[mid]:
				r=mid-1
			elif target>nums[mid]:
				l=mid+1
			else:
				r=mid
		if nums[l]==target:
			return l
		return -1

	def upper_bound(self,nums,l,r,target):
		while l<r:
			mid=(l+r+1)>>1 #!!!最重要，当l+r是奇数时，mid离r更近
			if target<nums[mid]:
				r=mid-1
			elif target>nums[mid]:
				l=mid+1
			else:
				l=mid
		if nums[r]==target:
			return l
		return -1



def  main():
	s=Solution()

	nums=[5,7,7,8,8,9]
	print s.searchRange(nums,8)
	

if __name__ == '__main__':
	main()