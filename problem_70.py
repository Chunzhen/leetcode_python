#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		num1=0
		num2=1
		s=0
		for i in range(n):
			s=num1+num2
			num1=num2
			num2=s
		return s

def main():
	solution=Solution()
	print solution.climbStairs(4)
	
if __name__ == '__main__':
  	main()  
