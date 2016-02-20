#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def findPeakElement(self,nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		r=self.find(nums,0,len(nums)-1)
		print 'r:',r
		if r==0:
			if nums[0]>nums[-1]:
				return 0
			else:
				return len(nums)-1
		else:
			return r

	def find(self,nums,l,r):
		while l<r:
			mid=l+(r-l)/2
			#print nums[mid-1],' ',nums[mid],' ',nums[mid+1]
			if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
				#print "bingo ",nums[mid]
				return mid
			else:
				if nums[l]<nums[mid-1] and nums[mid]<nums[mid-1]:
					r=mid
				elif nums[r]<nums[mid+1] and nums[mid]<nums[mid+1]:
					l=mid
				else:
					l_find=self.find(nums,l,mid)
					if l_find!=0:
						return l_find
					else:
						#print mid,' ',r
						r_find=self.find(nums,mid+1,r)
						if r_find!=0:
							return r_find
						else:
							return 0

		return 0



def  main():
	s=Solution()

	print s.findPeakElement([4,3,2,1,2,5,6,4])
	

if __name__ == '__main__':
	main()