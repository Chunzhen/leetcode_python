#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		nums1.extend(nums2)

		nums1=sorted(nums1)
		if len(nums1)%2==0:
		    return (nums1[len(nums1)/2-1]+ nums1[len(nums1)/2])/2.0
		else:
		    return nums1[len(nums1)/2]


def main():
	nums1=[2]
	nums2=[1,3,4]
	s=Solution()
	print s.findMedianSortedArrays(nums2,nums1)
	pass

if __name__ == '__main__':
	main()