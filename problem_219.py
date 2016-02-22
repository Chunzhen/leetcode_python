#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def containsNearbyDuplicate(self, nums,k):
		"""
		:type nums: List[int]
		type k: int
		:rtype: bool
		"""
		d={}
		for i in range(len(nums)):
			index=d.get(nums[i],-1)
			if index==-1:
				d[nums[i]]=i
			else:
				if i-index<=k:
					return True
				else:
					d[nums[i]]=i

		return False

def  main():
	s=Solution()
	print s.containsNearbyDuplicate([1,2,3,2,4,5,6,7,8,9,10],2)

if __name__ == '__main__':
	main()