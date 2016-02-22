#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def groupAnagrams(self,strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		d={}
		i=0
		l=[]
		for a in strs:
			s=''.join(sorted(a))
			index=d.get(s,-1)
			if index==-1:
				d[s]=i
				i+=1
				l.append([a])
			else:
				l[index].append(a)

		for i in range(len(l)):
			l[i]=sorted(l[i])
		return l



		

def  main():
	s=Solution()
	print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

if __name__ == '__main__':
	main()