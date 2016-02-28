#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
class Solution(object):
	def __init__(self):
		self.r_l=[]
	def combine(self,n,k):
		"""
		:type n: int 
		:type k: int
		:rtype: List[List[int]]
		"""
		self.r_l=[]
		self.find(n,1,k,[])
		return self.r_l

	def find(self,n,i,k,l):
		print l
		if len(l)==k:
			self.r_l.append(copy.deepcopy(l))
			return
		for i in range(i,n+1):
			l.append(i)
			self.find(n,i+1,k,l)
			l.pop()



def  main():
	s=Solution()

	print s.combine(4,2)
	#print 11>>1

if __name__ == '__main__':
	main()