#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def diffWaysToCompute(self,num,target):
		"""
		:type num: str
		:type target: int
		:rtype: List[int]
		"""
		if self.func(num) and int(num)==target:
			return num

		l=len(num)
		for i in range(l):
			

		
	def func(self,x):
		try:
			x=int(x)
			return isinstance(x,int)
		except ValueError:
			return False




		
def  main():
	s=Solution()
	input='15-7*6+24'
	print s.diffWaysToCompute(input)

if __name__ == '__main__':
	main()