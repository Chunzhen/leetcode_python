#! /usr/bin/env python
# -*- coding:utf-8 -*-

class NumArray(object):
	def __init__(self,nums):
		"""
		initialize your data structure here.
		:type nums:List[int]
		"""
		self.matrix=[]
		l=len(nums)
		s=0
		for i in range(l):
			s+=nums[i]
			self.matrix.append(s)

		print self.matrix

	def sumRange(self,i,j):
		"""
		sum of elements nums[i..j], inclusive.
		:type i: int
		:type j: int
		:rtype: int
		"""
		if i==0:
			return self.matrix[j]
		return self.matrix[j]-self.matrix[i-1]

def main():
	nums=[-2,0,3,-5,2,-1]
	arr=NumArray(nums)
	print arr.sumRange(0,2)
	print arr.sumRange(2,5)
	print arr.sumRange(0,5)
	

if __name__ == '__main__':
  	main()  
