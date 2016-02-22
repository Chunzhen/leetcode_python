#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def countPrimes(self,n):
		"""
		:type n: int
		:rtype: int
		"""
		isPrime=[]
		for i in range(n):
			isPrime.append(True)

		i=2
		while i*i<n:
			if not isPrime[i]: 
				i+=1
				continue
			j=i*i
			while j<n:
				isPrime[j]=False
				j+=i

			i+=1

		count=0
		for i in range(2,n):
			if isPrime[i]:
				count+=1

		return count

def  main():
	s=Solution()

	print s.countPrimes(10000)
	#print 11>>1

if __name__ == '__main__':
	main()