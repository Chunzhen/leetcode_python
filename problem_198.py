#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maxV_1=0
		maxV_2=0
		for i in range(len(nums)):
			tmp=maxV_1
			maxV_1=max(maxV_2+nums[i],maxV_1)
			maxV_2=tmp

		return max(maxV_1,maxV_2)

def main():
	solution=Solution()
	nums=[1,3,2,5,4,2,3]
	print solution.rob(nums)
	

if __name__ == '__main__':
  	main()  
