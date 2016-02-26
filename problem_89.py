# /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
	def grayCode(self,n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		l=[[0],[1]]

		for i in range(n-1):
			t_l=[]
			for inner_l in l:
				ll=[0]
				ll.extend(inner_l)
				t_l.append(ll)
			j=len(l)-1
			while j>=0:
				ll=[1]
				ll.extend(l[j])
				t_l.append(ll)
				j-=1
			#print t_l
			l=t_l
		r_l=[]
			
		for v in l:
			t=0
			for i in range(n):
				t+=v[i]*(2**(n-1-i))
			r_l.append(t)

		return r_l


def main():
	s=Solution()
	print s.grayCode(3)
	pass

# 1234
# 1243
# 1324
# 1343
# 1423
# 1432


if __name__ == '__main__':
	main()