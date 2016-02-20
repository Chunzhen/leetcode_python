#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
	def longestValidParentheses(self,s):
		"""
		:type s: str
		:rtype: int
		"""
		stack=[]
		longest=0
		l=0
		temp_l=0
		for v in s:
			if v=='(':
				stack.append('(')
			else:
				if len(stack)>0 and stack[-1]=='(':
					stack[-1]='1'
				else:
					stack.append(v)


		print stack
		r=""
		for v in stack:
			if str.isdigit(v):
				print "bingo"
				l+=1
			else:
				r+=v
				if l>longest:
					longest=l
				l=0
		if l>longest:
			longest=l

		print r
		return longest*2



def  main():
	s=Solution()

	print s.longestValidParentheses("(()())")

if __name__ == '__main__':
	main()