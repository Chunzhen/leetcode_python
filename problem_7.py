#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=True
        if x<0:
        	flag=False
        	x=abs(x)

        xx=str(x)
        r=0
        for i in range(len(xx)):
        	v=int(xx[i])
        	add=v*(10**i)
        	if sys.maxint-r<add:
        		return 0
        	else:
        		r+=add

        if not flag:
        	return -r
        return r
        	


def main():
	s=Solution()
	print sys.maxint
	print s.reverse(1534236469)
	pass

if __name__ == '__main__':
	main()
        