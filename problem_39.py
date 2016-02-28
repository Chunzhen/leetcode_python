#! /usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
	def __init__(self):
		self.r_l=[]
	def combinationSum(self,candidates,target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		self.r_l=[]
		candidates=sorted(candidates)
		self.find(candidates,0,target,'',0)
		return self.r_l

	def find(self,candidates,i,target,l,n):
		#print l
		if n==target:
			self.r_l.append([int(v) for v in l.split(',')])
			return
		elif n>target:
			return
		for i in range(i,len(candidates)):
			if l=='':
				self.find(candidates,i,target,str(candidates[i]),candidates[i])
			else:
				self.find(candidates,i,target,l+','+str(candidates[i]),n+candidates[i])



def  main():
	s=Solution()

	print s.combinationSum([2,3,6,7],7)
	#print 11>>1

if __name__ == '__main__':
	main()