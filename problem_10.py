#! /usr/bin/env python
# -*- coding:utf-8 -*-
!!! 未解决

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s)==0:
        	return True
        s_index=0
        last_p=0
        use_star=False
        for i in range(len(p)):
        	if p[i]=="*":
        		print "***"
        		if use_star:
        			print "use_star"
        			use_star=False
        			continue
        		while p[last_p]==s[s_index] or p[last_p]==".":
        			s_index+=1
        			if s_index==len(s):
        				last_p=i
        				break
        			print ".index"
        			print "s_index",s_index
        		if s_index==len(s):
        				last_p=i
        				break
        	elif p[i]==".":
        		s_index+=1
        		if s_index==len(s):
        				last_p=i
        				break
        	else:
        		print p[i]
        		print s_index
        		if p[i]==s[s_index]:
        			print "bingo"
        			s_index+=1
        			print "s_index",s_index
        			if s_index==len(s):
        				last_p=i
        				break
        		else:
        			if i+1<len(p) and p[i+1]=="*":
        				use_star=True
        				continue
        			else:
        				last_p=i
        				break

        	last_p=i
        
        print last_p
        print s_index
        if s_index==len(s) and (last_p==len(p)-1):
        	return True
        else:
        	return False
    
def main():
	s=Solution()
	print s.isMatch("aaa","a*a")

if __name__ == '__main__':
	main()