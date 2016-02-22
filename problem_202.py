#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def __init__(self):
		self.s=set([])
	def isHappy(self,n):
		"""
		:type n: ints
		:rtype: bool
		"""
		s_l=len(self.s)
		self.s.add(n)
		
		if s_l==len(self.s):
			return False
		if n==1:
			return True
		r=0
		while(n>0):
			new_n=n/10
			l=n-new_n*10
			r+=l**2
			n=new_n

		return self.isHappy(r)





		


def  main():
	s=Solution()

	print s.isHappy(19)
	#print 11>>1

if __name__ == '__main__':
	main()