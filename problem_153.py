#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def findMin(self,nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l=0
		r=len(nums)-1
		while l<r:
			
			mid=l+(r-l)/2
			print l,' ',r,' ',mid
			if nums[l]<nums[r]:
				break
			else:
				if nums[mid]>nums[r]:
					l=mid+1
					print "bingo"
				else:
					r-=1
					print "bingo2"

		
		print nums[l],' ',nums[r]
		return min(nums[l],nums[r])


def  main():
	s=Solution()

	nums=[7,0,1,2,3,4,5,6]
	print s.findMin(nums)

if __name__ == '__main__':
	main()