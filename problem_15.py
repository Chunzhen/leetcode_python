#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums=sorted(nums)
		l=len(nums)
		s=[]
		for i in range(l):
			if (i-1>=0 and nums[i-1]==nums[i]) or (nums[i]+2*nums[l-1]<0):
				continue
			for j in range(i+1,l):
				if (j-1>=i+1 and nums[j-1]==nums[j]) or (nums[i]+nums[j]+nums[l-1]<0):
					continue
				for k in range(j+1,l):
					if k-1>=j+1 and nums[k-1]==nums[k]:
						continue
					if nums[i]+nums[j]+nums[k]==0:
						s.append([nums[i],nums[j],nums[k]])
					elif nums[i]+nums[j]+nums[k]>0:
						break

		return s


def  main():
	s=Solution()
	nums=[-1,0,1,2,-1,-4]#
	print s.threeSum(nums)
	pass

if __name__ == '__main__':
	main()