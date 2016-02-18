#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def removeDuplicates(self,nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums)<2:
			return len(nums)
		c=nums[0]-1
		l=0
		for v in nums:
			if c!=v:
				nums[l]=v
				c=v
				l+=1

		return l

		


def  main():
	s=Solution()

	print s.removeDuplicates([1,1,2])

if __name__ == '__main__':
	main()