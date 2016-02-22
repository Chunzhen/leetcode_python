#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def getHint(self,secret,guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		d={}
		for v in secret:
			n=d.get(v,0)
			d[v]=n+1

		bull=0
		cow=0
		for i in range(len(guess)):
			if guess[i]==secret[i]:
				bull+=1
				d[secret[i]]=d.get(secret[i],0)-1

		for i in range(len(guess)):
			if guess[i]!=secret[i] and guess[i] in d and d[guess[i]]>0:
				cow+=1
				d[guess[i]]=d[guess[i]]-1

		return str(bull)+'A'+str(cow)+'B'

		

def  main():
	s=Solution()
	print s.getHint('1122','2211')

if __name__ == '__main__':
	main()