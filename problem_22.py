#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def generateParenthesis(self,n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n==0:
			return []
		s=['(']
		for i in range(1,2*n):
			temp=[]
			for v in s:
				if self.is_valid(v+'(',n):
					temp.append(v+'(')
				if self.is_valid(v+')',n):
					temp.append(v+')')
				
			s=temp
		return s

	def is_valid(self,s,n):
		stack=[]
		l=0
		for v in s:
			if v=='(':
				stack.append(v)
			else:
				if len(stack)==0:
					return False
				else:
					l+=1
					stack=stack[0:-1]

		if len(stack)+l>n:
			return False
		else:
			return True

def  main():
	s=Solution()

	print s.generateParenthesis(3)

if __name__ == '__main__':
	main()