#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def isPalindrome(self,x):
		"""
		: type x: int
		: rtype: bool
		"""
		if x<0:
			return False

		x=str(x)
		l=len(x)
		for i in range(l/2):
			if x[i]!=x[l-i-1]:
				return False
		return True


def main():
	s=Solution()
	print s.isPalindrome(123210)

if __name__ == '__main__':
	main()