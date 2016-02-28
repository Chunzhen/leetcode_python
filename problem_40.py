#! /usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
	def __init__(self):
		self.r_l=set()
	def combinationSum2(self,candidates,target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		self.r_l=set()
		candidates=sorted(candidates)
		self.find(candidates,0,target,'',0)
		r=[]
		for l in self.r_l:
			r.append([int(v) for v in l.split(',')])
		return r

	def find(self,candidates,j,target,l,n):
		print l
		if n==target:
			self.r_l.add(l)
			return True
		elif n>target:
			return True
		for i in range(j,len(candidates)):
			if l=='':
				r=self.find(candidates,i+1,target,str(candidates[i]),candidates[i])
				if r:
					break
			else:
				r=self.find(candidates,i+1,target,l+','+str(candidates[i]),n+candidates[i])
				if r:
					break



def  main():
	s=Solution()

	print s.combinationSum2([10,1,2,7,6,1,5],8)
	#print 11>>1

if __name__ == '__main__':
	main()