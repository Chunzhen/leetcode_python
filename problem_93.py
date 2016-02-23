#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def __init__(self):
		self.l=[]
	def restoreIpAddresses(self,s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		self.l=[]
		self.find(s, 0, 4, [])
		return self.l

	def find(self,s,i,n,tmp_l):
		if n==1 and ((s[i]!='0' and int(s[i:])<256) or i==len(s)-1):
			self.l.append(''.join(tmp_l)+s[i:])
			return True
		elif n==0 and i!=len(s)-1:
			return False
		
		if i<len(s)-1:
			tmp_l.append(s[i]+'.')
			b1=self.find(s,i+1,n-1,tmp_l)
			tmp_l.pop()

		if i+2<len(s) and s[i]!='0':
			tmp_l.append(s[i:i+2]+'.')
			b2=self.find(s,i+2,n-1,tmp_l)
			tmp_l.pop()

		if i+3<len(s) and s[i]!='0' and  int(s[i:i+3])<256:
			tmp_l.append(s[i:i+3]+'.')
			b3=self.find(s,i+3,n-1,tmp_l)
			tmp_l.pop()

def  main():
	s=Solution()
	print s.restoreIpAddresses('010010')

if __name__ == '__main__':
	main()