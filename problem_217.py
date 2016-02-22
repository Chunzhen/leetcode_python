#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		return not len(nums)==len(set(nums))

def  main():
	s=Solution()


if __name__ == '__main__':
	main()