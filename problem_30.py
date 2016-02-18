#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
class Solution(object):
	def findSubstring(self,s,words):
		"""
		:type s: str
		:type words: List[str]
		:rtype: List[int]
		"""
		l=len(words[0])
		words_len=len(words)
		set_words=set(words)
		dd={}
		for word in words:
			temp=dd.get(word,0)
			dd[word]=temp+1

		r=[]
		for i in range(len(s)-l+1):
			find_i=self.find(copy.deepcopy(dd),i,s,l,words,words_len)
			if find_i==i:
				r.append(i)

		return r
	def find(self,d,i,s,l,words,words_len):
		tt_l=0
		for j in range(i,len(s)-l+1,l):
			t_s=s[j:j+l]
			temp_l=d.get(t_s,0)
			if temp_l==0:
				return -1

			temp_l-=1
			d[t_s]=temp_l
			tt_l+=1

			if tt_l==words_len:
				return i

		
def  main():
	s=Solution()

	print s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])

if __name__ == '__main__':
	main()