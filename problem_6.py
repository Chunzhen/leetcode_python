#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
        	return s
        row=[]
        for i in range(numRows):
        	row.append("")
        n=numRows*2-2
        for x in range(len(s)):
        	left=x%n
        	if left>=numRows:
        		left=(numRows-1)*2-left
        	row[left]+=s[x]
        	
        return "".join(row)

def main():
	s=Solution()
	print s.convert("",2)
	pass

if __name__ == '__main__':
	main()
        