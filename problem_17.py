#! /usr/bin/env python
# -*- coding:utf-8 -*-

import copy

class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		d={
		'2':['a','b','c'],
		'3':['d','e','f'],
		'4':['g','h','i'],
		'5':['j','k','l'],
		'6':['m','n','o'],
		'7':['p','q','r','s'],
		'8':['t','u','v'],
		'9':['w','x','y','z']
		}
		s=[]
		for v in digits:
			temp_s=[]
			for v2 in d[v]:
				if len(s)==0:
					temp_s.append(v2)
				else:
					for v3 in s:
						temp_s.append(v3+v2)
			s=temp_s

		return list(s)



def  main():
	s=Solution()
	digits="23"
	print s.letterCombinations(digits)

if __name__ == '__main__':
	main()