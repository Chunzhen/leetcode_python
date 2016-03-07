#! /usr/bin/env python 
#! -*- coding:utf-8 -*-

class Solution(object):
	def maxSubArray(self,nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		m=nums[0]
		l=nums[0]
		for i in range(1,len(nums)):
			l=max(nums[i],nums[i]+l)
			if l>m:
				m=l
		return m

def main():
	nums=[-2,1,-3,4,-1,2,1,-5,4]
	s=Solution()
	print s.maxSubArray(nums)
	pass

if __name__ == '__main__':
	main()