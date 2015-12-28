#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_len=0
        all_set=set(s)
        s_set=set()
        s2=""
        inner_start=0
        for k1 in range(len(s)):
        	temp_len=len(s_set)
        	if len(s)-inner_start+len(s_set)<=r_len or r_len==len(all_set):
        		break
        	for k2 in range(inner_start,len(s)):
        		if s[k2] not in s_set:
        			s_set.add(s[k2])     			
        			temp_len+=1
        		else:
        			s_set.remove(s[k1])
        			inner_start=k2	
        			break
        	if r_len<temp_len:
        		r_len=temp_len

        return r_len


def main():
	s=Solution()
	print s.lengthOfLongestSubstring("dvdf")
	pass

if __name__ == '__main__':
	main()
