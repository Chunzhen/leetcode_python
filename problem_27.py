#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def removeElement(self,nums,val):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l=0
		for v in nums:
			if val!=v:
				nums[l]=v
				l+=1

		print nums
		return l

		


def  main():
	s=Solution()

	print s.removeElement([1,1,2],1)

if __name__ == '__main__':
	main()