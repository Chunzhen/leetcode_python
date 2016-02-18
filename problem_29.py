#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class Solution(object):
	def divide(self,dividend,divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		r=2147483647

		try:
			r=float(dividend)/float(divisor)
			r=int(r)
		except:
			pass
		if r>2147483647:
			r=2147483647
		return r

		


def  main():
	s=Solution()

	print s.divide(-2147483648,-1)

if __name__ == '__main__':
	main()