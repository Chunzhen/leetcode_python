#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def search(self,nums,target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		l=0
		r=len(nums)-1

		while l<=r:
			mid=l+(r-l)/2
			#print mid,' ',l,' ',r
			if target==nums[mid]:
				return mid
			elif target>nums[mid]:
				if nums[l]<nums[r]:
					l=mid+1
				else:
					if target==nums[r]:
						return r
					elif target>nums[r]:
						r-=1
					else:
						l+=1

			elif target<nums[mid]:
				if nums[l]<nums[r]:
					r=mid-1
					#print 'bingo'
				else:
					if target==nums[l]:
						return l
						
					elif target<nums[l]:
						l+=1

					if target==nums[r]:
						return r
					elif target>nums[r]:
						r-=1

		return -1

def  main():
	s=Solution()

	nums=[3,1,2]
	for v in nums:
		print s.search(nums,v)
		print ""
	#print 11>>1

if __name__ == '__main__':
	main()