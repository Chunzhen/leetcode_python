#! /usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
	def __init__(self):
		self.r_l=set()
	def combinationSum3(self,k,target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		self.r_l=set()
		candidates=[i for i in range(1,10)]
		self.find(candidates,0,target,'',0,0,k)
		r=[]
		for l in self.r_l:
			r.append([int(v) for v in l.split(',')])
		return r

	def find(self,candidates,j,target,l,len_l,n,k):
		print l
		if n==target and len(l.split(','))==k:
			self.r_l.add(l)
			return True
		elif n>target:
			return True
		for i in range(j,len(candidates)):
			if n+candidates[i]<=target and len_l<=k:
				if l=='':
					r=self.find(candidates,i+1,target,str(candidates[i]),1,candidates[i],k)
					if r:
						break
				else:
					r=self.find(candidates,i+1,target,l+','+str(candidates[i]),len_l+1,n+candidates[i],k)
					if r:
						break



def  main():
	s=Solution()

	print s.combinationSum3(3,15)
	#print 11>>1

if __name__ == '__main__':
	main()