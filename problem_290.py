#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def wordPattern(self,pattern,s):
		"""
		:type pattern: str
		:type s: str
		:rtype: bool
		"""
		s=s.split(' ')
		t=pattern
		if len(s)!=len(t):
			return False
		d1={}
		d2={}
		for i in range(len(s)):
			n1=d1.get(s[i],-1)
			n2=d2.get(t[i],-1)
			if n1!=n2:
				return False
			if n1==-1:
				n1=len(d1)+1
				d1[s[i]]=n1
			if n2==-1:
				n2=len(d2)+1
				d2[t[i]]=n2

		return True
		

def  main():
	s=Solution()
	print s.wordPattern('abba','dog cat cat fish')

if __name__ == '__main__':
	main()