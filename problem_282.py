#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def __init__(self):
		self.res=[]
	def addOperators(self,num,target):
		"""
		:type num: str
		:type target: int
		:rtype: List[int]
		"""
		self.res=[]
		self.add(num,target,'',0,0)
		return self.res

		
	def add(self,num,target,tmp,curRes,preNum):
		if curRes==target and len(num)==0:
			self.res.append(tmp)
			return

		for i in range(len(num)):
			curStr=num[0:i+1]
			print curStr
			if len(curStr)>1 and curStr[0]=='0':
				return

			curNum=int(curStr)
			next=num[i+1:]

			if len(tmp)==0:
				self.add(next,target,curStr,curNum,curNum)
			else:
				self.add(next,target,tmp+'*'+str(curNum),(curRes-preNum)+preNum*curNum,preNum*curNum)
				self.add(next,target,tmp+'-'+str(curNum),curRes-curNum,-curNum)
				self.add(next,target,tmp+'+'+str(curNum),curRes+curNum,curNum)




		
def  main():
	s=Solution()
	
	print s.addOperators('123',6)

if __name__ == '__main__':
	main()