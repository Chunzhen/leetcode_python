#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
class Solution(object):
	def __init__(self):
		self.n=0
		self.p=""
	def getPermutation(self,n,k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		self.n=0
		self.p=""
		nums=[i for i in range(1,n+1)]
		self.find(nums,[],len(nums),k)
		return self.p

	def find(self,nums,tmp_l,n,k):
		if len(tmp_l)==n:
			self.n+=1

			if self.n==k:
				self.p=''.join([str(v) for v in tmp_l])
				return True
			return False
		for i in range(len(nums)):
			tmp_l.append(nums[i])
			new=nums[0:i]
			if new:
				new.extend(nums[i+1:])
			else:
				new=nums[i+1:]
			r=self.find(new,tmp_l,n,k)
			if r:
				return True
			tmp_l.pop()

def main():
	s=Solution()
	print s.getPermutation(5,2)

if __name__ == '__main__':
	main()