#! /usr/bin/env python 
#! -*- coding:utf-8 -*-

class Solution(object):
	def numDecodings(self,s):
		"""
		:type s: str
		:rtype: int 
		"""
		l=len(s)
		if l==0 or (l==1 and s=='0'):
			return 0
		elif l==1:
			return 1
		nums=[0 for i in range(l)]	
		
		t=int(s[0])
		t2=int(s[1])
		if t!=0:
			nums[0]=1
		if t==1 and t2>0  or (t==2 and t2>0 and t2<7):
			nums[1]=2
		elif (t==1 or t==2) and t2==0:
			nums[1]=1
		elif t2>0:
			nums[1]=nums[0]
		for i in range(2,l):
			t=int(s[i-1])
			t2=int(s[i])
			if t==1 and t2>0  or (t==2 and t2>0 and t2<7):
				nums[i]=nums[i-1]+nums[i-2]
			elif (t==1 or t==2) and t2==0:
				nums[i]=nums[i-2]
			elif t2>0:
				nums[i]=nums[i-1]
		print nums
		return nums[-1]

def main():
	s=Solution()
	print s.numDecodings('110')
	pass

if __name__ == '__main__':
	main()