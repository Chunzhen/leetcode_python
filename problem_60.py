# /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
	def getPermutation(self,n,k):
		l=[]
		l2=[]
		k-=1
		for i in range(1,n):
			if i==1:
				l.append(1)
			else:
				l.append(l[-1]*i)
			l2.append(i)
		l2.append(n)
		#print l
		#print l2
		i=len(l)-1
		r=[]
		while i>=0:
			index=k//l[i]
			#print index,' ',k,' ',l2[index]
			r.append(str(l2[index]))
			l2.remove(l2[index])
			k=k-l[i]*index
			i-=1

		r.append(str(l2[0]))
		return ''.join(r)

def main():
	s=Solution()
	print s.getPermutation(9,171669)
	pass

# 1234
# 1243
# 1324
# 1343
# 1423
# 1432


if __name__ == '__main__':
	main()