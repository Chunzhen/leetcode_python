#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def mySqrt(self,x):
		"""
		:type x: int
		:rtype: int
		"""
		l=0
		r=x

		while(l<=r):
			mid=l+(r-l)/2
			if x<mid**2:
				r=mid-1
			elif x>mid**2:
				l=mid+1
			else:
				return mid

		return min(l,r)
		



def  main():
	s=Solution()

	print s.mySqrt(15)
	

if __name__ == '__main__':
	main()