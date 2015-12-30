#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs)==0:
			return ""
		i=0
		r_str=""
		while True:
			for j in range(1,len(strs)):
				if i<len(strs[0]) and i<len(strs[j]) and strs[j][i]==strs[0][i]:
					pass
				else:
					return r_str

			if i>=len(strs[0]):
				break
			r_str+=strs[0][i]
			i+=1			

		return r_str


def main():
	solution=Solution()
	print solution.longestCommonPrefix([""])
	

if __name__ == '__main__':
  	main()  
