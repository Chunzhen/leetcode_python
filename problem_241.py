#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def diffWaysToCompute(self,input):
		"""
		:type input: str
		:rtype: List[int]
		"""
		r_list=[]
		l=len(input)
		for i in range(l):
			if input[i]=='+' or input[i]=='-' or input[i]=='*':
				left=self.diffWaysToCompute(input[0:i])
				right=self.diffWaysToCompute(input[i+1:])
				for j in range(len(left)):
					for k in range(len(right)):
						if input[i]=='+':
							r_list.append(left[j]+right[k])
						elif input[i]=='-':
							r_list.append(left[j]-right[k])
						else:
							r_list.append(left[j]*right[k])

		if len(r_list)==0:
			r_list.append(int(''.join(input)))
		return r_list





		
def  main():
	s=Solution()
	input='15-7*6+24'
	print s.diffWaysToCompute(input)

if __name__ == '__main__':
	main()