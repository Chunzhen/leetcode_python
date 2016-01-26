#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack=[]
		d={'{':'}','[':']','(':')'}

		for v in s:
			print v
			print stack
			if v=='(' or v=='{' or v=='[':
				stack.append(v)
			else:
				if len(stack)==0 or d[stack[-1]]!=v:
					return False
				else:
					stack=stack[0:-1]

		if len(stack)==0:
			return True
		else:
			return False

def  main():
	s=Solution()
	ss="()[]{}{"

	print s.isValid(ss)

if __name__ == '__main__':
	main()