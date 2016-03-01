#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def __init__(self):
		self.qSet=set()
	def totalNQueens(self,n):
		"""
		:type n: int
		:rtype: int
		"""
		board=[]
		for i in range(n):
			l=[]
			for j in  range(n):
				l.append('.')
			board.append(l)

		row_set=[]
		col_set=[]
		left_set=[]
		right_set=[]
		for i in range(n):
			row_set.append(False)
			col_set.append(False)

		for i in range(2*n-1):
			left_set.append(False)
			right_set.append(False)

		self.find(board,0,n,0,row_set,col_set,left_set,right_set)
		return len(self.qSet)


	def find(self,board,k,n,a,row_set,col_set,left_set,right_set):
		#print board
		if k==n:
			s=''
			for i in range(n):
				s+=''.join(board[i])

			self.qSet.add(s)
			return True

		for i in range(a,n):
			for j in range(n):
				if self.check(board, i, j, n,row_set,col_set,left_set,right_set) and board[i][j]!='Q':
					board[i][j]='Q'
					row_set[i]=True
					col_set[j]=True
					left_set[i+j]=True
					right_set[n-1-i+j]=True
					r=self.find(board,k+1,n,i+1,row_set,col_set,left_set,right_set)
					board[i][j]='.'
					row_set[i]=False
					col_set[j]=False
					left_set[i+j]=False
					right_set[n-1-i+j]=False
			return False

		return False


	def check(self,board,i,j,n,row_set,col_set,left_set,right_set):
		if row_set[i] or col_set[j] or left_set[i+j] or right_set[n-1-i+j]:
			return False
		return True


def  main():
	s=Solution()

	print s.solveNQueens(4)
	

if __name__ == '__main__':
	main()