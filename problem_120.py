#! /usr/bin/env python 
#! -*- coding:utf-8 -*-

class Solution(object):
	def minimumTotal(self,triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		l=len(triangle)
		for i in range(l-1,0,-1):
			for j in range(1,i+1):
				triangle[i-1][j-1]+=min(triangle[i][j],triangle[i][j-1])
		return triangle[0][0]

def main():
	nums=[-2,1,-3,4,-1,2,1,-5,4]
	s=Solution()
	triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
	print s.minimumTotal(triangle)
	pass

if __name__ == '__main__':
	main()