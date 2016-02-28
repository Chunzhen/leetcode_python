#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def solveSudoku(self,board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		row_set,col_set,matrix_set=self.isValidSudoku(board)
		self.find(board, row_set, col_set, matrix_set,0)

	def isValidSudoku(self,board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		row_set=[]
		col_set=[]
		for i in range(9):
			s1=set([])
			s2=set([])
			for j in range(9):
				if board[i][j]!='.':
					s1.add(board[i][j])

				if board[j][i]!='.':
					s2.add(board[j][i])

			row_set.append(s1)
			col_set.append(s2)

		matrix_set=[]
		for i in range(9):
			b=i%3*3
			c=(i/3)*3
			s1=set([])
			for j in range(3):
				for k in range(3):
					if board[j+b][k+c]!='.':
						s1.add(board[j+b][k+c])

			matrix_set.append(s1)

		return row_set,col_set,matrix_set

	def find(self,board,row_set,col_set,matrix_set,b):
		flag=True
		for i in range(b,9):
			for j in range(9):
				if board[i][j]=='.':
					flag=False
					for k in range(1,10):
						k=str(k)
						a=j/3*3+i/3

						if k not in row_set[i] and k not in col_set[j] and k not in matrix_set[a]:
							board[i][j]=k
							row_set[i].add(k)
							col_set[j].add(k)
							matrix_set[a].add(k)
							r=self.find(board,row_set,col_set,matrix_set,i)
							#return r
							if r:
								return True
							board[i][j]='.'	
							row_set[i].remove(k)
							col_set[j].remove(k)
							matrix_set[a].remove(k)

					return False
						
		return flag

	def print_board(self,board):
		for i in range(9):
			print ''.join(board[i])

def  main():
	s=Solution()

	n=2126753390
	# print s.solveSudoku([
	# 	['5','3','4','6','7','8','9','1','2'],
	# 	['6','7','2','1','9','5','3','4','8'],
	# 	['1','9','8','3','4','2','5','6','7'],
	# 	['8','5','9','7','6','1','4','2','3'],
	# 	['4','2','6','8','5','3','7','9','1'],
	# 	['7','1','3','9','2','4','8','5','6'],
	# 	['9','6','1','5','3','7','2','8','4'],
	# 	['2','8','7','4','1','9','6','3','.'],
	# 	['3','4','5','2','8','6','1','7','9']
	# 	])
	board=[
		['5','3','.','.','7','.','.','.','.'],
		['6','.','.','1','9','5','.','.','.'],
		['.','9','8','.','.','.','.','6','.'],
		['8','.','.','.','6','.','.','.','3'],
		['4','.','.','8','.','3','.','.','1'],
		['7','.','.','.','2','.','.','.','6'],
		['.','6','.','.','.','.','2','8','.'],
		['.','.','.','4','1','9','.','.','5'],
		['.','.','.','.','8','.','.','7','9']
		]
	print s.solveSudoku(board)
	s.print_board(board)

		
	#print 11>>1

if __name__ == '__main__':
	main()