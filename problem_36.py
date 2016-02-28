#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def isValidSudoku(self,board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		s1=set([])
		s2=set([])
		for i in range(9):
			s1=set([])
			s2=set([])
			k1=0
			k2=0
			for j in range(9):
				if board[i][j]!='.':
					s1.add(board[i][j])
					k1+=1

				if board[j][i]!='.':
					s2.add(board[j][i])
					k2+=1

			if len(s1)!=k1:
				return False
			if len(s2)!=k2:
				return False

		for i in range(9):
			b=i%3*3
			c=(i/3)*3

			#print b,' ',c
			s1=set([])
			a=0
			for j in range(3):
				for k in range(3):
					#print (j+b),' ',(k+c)
					if board[j+b][k+c]!='.':
						s1.add(board[j+b][k+c])
						a+=1

			#print ' '
			if len(s1)!=a:
				return False

		return True




		


def  main():
	s=Solution()

	n=2126753390
	print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
	#print 11>>1

if __name__ == '__main__':
	main()