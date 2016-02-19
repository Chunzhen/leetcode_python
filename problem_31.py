#! /usr/bin/env python
# -*- coding:utf-8 -*-

#思路比较重要！
import copy
class Solution(object):
	def nextPermutation(self,nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		l=len(nums)
		i=l-1

		while(i>0):
			if nums[i-1]<nums[i]:
				j=l-1
				while(j>i):
					if nums[j]>nums[i-1]:
						break
					j-=1
				self.swap(nums, i-1, j)
				for j in range((l-1-i)/2+1):
					self.swap(nums,j+i,l-1-j)
				return

			i-=1

		for j in range((l-1)/2+1):
			self.swap(nums,j,l-1-j)
		return

	def swap(self,nums,i,j):
		temp1=nums[i]
		nums[i]=nums[j]
		nums[j]=temp1

def  main():
	s=Solution()

	nums=[2,3,1]
	s.nextPermutation(nums)
	print nums

if __name__ == '__main__':
	main()