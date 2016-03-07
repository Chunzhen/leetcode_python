#! /usr/bin/env python 
#! -*- coding:utf-8 -*-

class Solution(object):
	def uniquePaths(self,m,n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		board=[]
		for i in range(m):
			l=[0 for j in range(n)]
			board.append(l)
		self.path(m-1,n-1,board)
		return board[m-1][n-1]

	def path(self,m,n,board):
		if m==0:
			board[m][n]=1
		elif n==0:
			board[m][n]=1
		else:
			if board[m][n-1]==0:
				self.path(m,n-1, board)
			if board[m-1][n]==0:
				self.path(m-1,n,board)
			board[m][n]=board[m][n-1]+board[m-1][n]

def main():
	nums=[-2,1,-3,4,-1,2,1,-5,4]
	s=Solution()
	print s.uniquePaths(23,12)
	pass

if __name__ == '__main__':
	main()