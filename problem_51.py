#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def __init__(self):
		self.qSet=set()
	def solveNQueens(self,n):
		"""
		:type n: int
		:rtype: List[List[str]]
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
		r_list=[]
		for q in self.qSet:
			l=[]
			for i in range(n):
				l.append(q[i*n:(i+1)*(n)])
			r_list.append(l)

		return r_list


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
					# if r:
					# 	return True
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

		# for a in range(n):
		# 	if a!=j and board[i][a]=='Q':
		# 		return False
		# 	if a!=i and board[a][j]=='Q':
		# 		return False

		# a=i
		# b=j
		# while a>=0 and b>=0:
		# 	if board[a][b]=='Q':
		# 		return False
		# 	a-=1
		# 	b-=1 

		# a=i
		# b=j
		# while a<n and b<n:
		# 	if board[a][b]=='Q':
		# 		return False
		# 	a+=1
		# 	b+=1

		# a=i
		# b=j
		# while a>=0 and b<n:
		# 	if board[a][b]=='Q':
		# 		return False
		# 	a-=1
		# 	b+=1

		# a=i
		# b=j
		# while a<n and b>=0:
		# 	if board[a][b]=='Q':
		# 		return False
		# 	a+=1
		# 	b-=1

		# return True


def  main():
	s=Solution()

	print s.solveNQueens(8)
	

if __name__ == '__main__':
	main()