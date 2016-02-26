# /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
	def __init__(self):
		self.d={}
	def partition(self,s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		l=[]
		self.dfs(s,'',len(s),l,0)
		return l

	def dfs(self,s,tmp_l,n,l,all_len):
		if all_len==n:
			l.append(tmp_l.split(','))

		for j in range(1,len(s)+1):
			ss=s[0:j]
			inD=self.d.get(ss,-1)
			if inD!=0:
				if inD==1 or self.isPalindrome(ss):
					if len(tmp_l)!=0:
						self.dfs(s[j:],tmp_l+','+ss,n,l,all_len+j)
					else:
						self.dfs(s[j:],tmp_l+ss,n,l,all_len+j)
					self.d[ss]=1
				else:
					self.d[ss]=0

	def isPalindrome(self,s):
		for i in range(len(s)//2):
			if s[i]!=s[len(s)-1-i]:
				return False
		return True


		

def main():
	s=Solution()
	print s.partition('cbbbcc')
	pass

# 1234
# 1243
# 1324
# 1343
# 1423
# 1432


if __name__ == '__main__':
	main()