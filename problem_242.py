#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def isAnagram(self,s,t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False
		d1={}
		d2={}
		for i in range(len(s)):
			n1=d1.get(s[i],0)
			n2=d2.get(t[i],0)
			d1[s[i]]=n1+1
			d2[t[i]]=n2+1

		if len(d1)!=len(d2):
			return False

		for k,n in d1.items():
			if d2.get(k,-1)!=n:
				return False

		return True
		

def  main():
	s=Solution()
	print s.isAnagram('anagram','nagaram')

if __name__ == '__main__':
	main()