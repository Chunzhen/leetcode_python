#! /usr/bin/env python
# -*- coding:utf-8 -*-

def isBadVersion(version):
	if version>1702766718:
		return True
	else:
		return False

class Solution(object):
	def firstBadVersion(self,n):
		"""
		:type n: int
		:rtype: int
		"""
		l=1
		r=n
		i=0
		while l<=r:
			mid=l+(r-l+1)/2

			if isBadVersion(mid):
				r=mid-1
				if not isBadVersion(r):
					return mid
			else:
				l=mid+1

			i+=1

		if isBadVersion(r):
			return r

		return -1


def  main():
	s=Solution()

	n=2126753390
	print s.firstBadVersion(n)
	#print 11>>1

if __name__ == '__main__':
	main()