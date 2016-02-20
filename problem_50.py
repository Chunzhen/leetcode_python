#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def myPow(self,x,n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n>0:
			if n%2==0:
				return self.myPow(x*x,n/2)
			else:
				return self.myPow(x*x,n/2)*x	
		elif n==1:
			return x
		elif n==0:
			return 1
		else:
			return self.myPow(1/x,-n)
		



		



def  main():
	s=Solution()

	print s.myPow(2.0,-3)
	

if __name__ == '__main__':
	main()