#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def fractionToDecimal(self,numerator,denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		is_fu=False
		if (numerator<0 and denominator>0) or (numerator>0 and denominator<0):
			is_fu=True

		if numerator<0:
			numerator=-numerator
		if denominator<0:
			denominator=-denominator

		n=numerator//denominator
		numerator=numerator-n*denominator
		if numerator==0:
			if is_fu:
				return "-"+str(n)
			return str(n)
		l=[str(n),'.']
	 	d={}
	 	i=2
	 	while True:
	 		n=numerator*10
	 		index=d.get(n,-1)
	 		left=n//denominator
	 		numerator=n-left*denominator

	 		if numerator==0:
	 			l.append(str(left))
	 			break
	 		if index==-1:
	 			d[n]=i
	 			i+=1
	 			l.append(str(left))
	 		else:
	 			l.insert(index,'(')
	 			l.append(')')
	 			break

	 	if is_fu:
	 		return '-'+''.join(l)
	 	return ''.join(l)



		

def  main():
	s=Solution()
	print s.fractionToDecimal(-50,8)

if __name__ == '__main__':
	main()