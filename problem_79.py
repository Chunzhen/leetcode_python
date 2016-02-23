#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1(object):
	def exist(self,board,word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.find(board,word,i,j,0,set([])):
					return True
		return False

	def find(self,board,word,i,j,k,l):
		s=(str(i)+','+str(j))
		if board[i][j]== word[k] and s not in l:
			l.add(s)
			b1=False
			b2=False
			b3=False
			b4=False
			if k==len(word)-1:
				return True
			if i-1>=0:
				b1=self.find(board,word,i-1,j,k+1,l)
			if j-1>=0:
				b2=self.find(board,word,i,j-1,k+1,l)
			if i+1<len(board):
				b3=self.find(board,word,i+1,j,k+1,l)
			if j+1<len(board[0]):
				b4=self.find(board,word,i,j+1,k+1,l)

			if b1 or b2 or b3 or b4:
				return True
			else:
				l.remove(s)
				return False

		else:
			return False

class Solution(object):
	def exist(self,board,word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		l=[]
		for i in range(len(board)):
			t=[]
			for j in range(len(board[0])):
				t.append(False)
			l.append(t)


		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.find(board,word,i,j,0,l):
					return True
		return False

	def find(self,board,word,i,j,k,l):
		s=(str(i)+','+str(j))
		if board[i][j]== word[k] and not l[i][j]:
			l[i][j]=True
			b1=False
			b2=False
			b3=False
			b4=False
			if k==len(word)-1:
				return True
			if i-1>=0:
				b1=self.find(board,word,i-1,j,k+1,l)
			if j-1>=0:
				b2=self.find(board,word,i,j-1,k+1,l)
			if i+1<len(board):
				b3=self.find(board,word,i+1,j,k+1,l)
			if j+1<len(board[0]):
				b4=self.find(board,word,i,j+1,k+1,l)

			if b1 or b2 or b3 or b4:
				return True
			else:
				l[i][j]=False
				return False

		else:
			return False

def  main():
	s=Solution()
	print s.exist(['AB'],'BA')

if __name__ == '__main__':
	main()