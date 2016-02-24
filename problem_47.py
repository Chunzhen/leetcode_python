#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
class Solution(object):
	def __init__(self):
		self.l=[]
	def permuteUnique(self,nums):
		"""
		:type nums: List[int] 
		:rtype: List[List[str]]
		"""
		self.l=[]
		self.find(nums,[],len(nums))
		return self.l

	def find(self,nums,tmp_l,n):
		#print tmp_l
		#print 'nums: ',nums
		if len(tmp_l)==n:
			self.l.append(copy.deepcopy(tmp_l))
			return
		tmp_nums=set(nums)
		tmp_nums=[x for x in tmp_nums]
		nums2=copy.deepcopy(nums)
		l=len(tmp_nums)

		for v in tmp_nums:
			tmp_l.append(v)
			nums2.remove(v)
			self.find(nums2,tmp_l,n)
			tmp_l.pop()
			nums2.append(v)

def main():
	s=Solution()
	print s.permuteUnique([1,1,2,2])

if __name__ == '__main__':
	main()