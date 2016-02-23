#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
class Solution(object):
	def __init__(self):
		self.l=[]
	def permute(self,nums):
		"""
		:type nums: List[int] 
		:rtype: List[List[str]]
		"""
		self.l=[]
		self.find(nums,[],len(nums))
		return self.l

	def find(self,nums,tmp_l,n):
		if len(tmp_l)==n:
			self.l.append(copy.deepcopy(tmp_l))
			return
		l=len(nums)
		for i in range(l):
			tmp_l.append(nums[i])
			new=nums[0:i]
			if new:
				new.extend(nums[i+1:])
			else:
				new=nums[i+1:]
			self.find(new,tmp_l,n)
			tmp_l.pop()

def main():
	s=Solution()
	print s.permute([1,2,3])

if __name__ == '__main__':
	main()