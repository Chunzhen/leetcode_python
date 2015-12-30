#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		roman_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
		roman_str=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
		r_int=0
		i=0
		l_s=len(s)
		while i<l_s:
			for j in range(len(roman_num)):
				if len(roman_str[j])==1:
					if s[i]==roman_str[j]:
						r_int+=roman_num[j]
						i+=1
						break
				else:
					if s[i]==roman_str[j][0] and i+1<l_s and s[i+1]==roman_str[j][1]:
						r_int+=roman_num[j]
						i+=2
						break

			# if s[i]=="M":
			# 	r_int+=1000
			# 	i+=1
			# elif s[i]=="C" and i+1<len(s) and s[i+1]=="M":
			# 	r_int+=900
			# 	i+=2
			# elif s[i]=="D":
			# 	r_int+=500
			# 	i+=1
			# elif s[i]=="C" and i+1<len(s) and s[i+1]=="D":
			# 	r_int+=400
			# 	i+=2
			# elif s[i]=="C":
			# 	r_int+=100
			# 	i+=1
			# elif s[i]=="X" and i+1<len(s) and s[i+1]=="C":
			# 	r_int+=90
			# 	i+=2
			# elif s[i]=="L":
			# 	r_int+=50
			# 	i+=1
			# elif s[i]=="X" and i+1<len(s) and s[i+1]=="L":
			# 	r_int+=40
			# 	i+=2
			# elif s[i]=="X":
			# 	r_int+=10
			# 	i+=1
			# elif s[i]=="I" and  i+1<len(s) and s[i+1]=="X":
			# 	r_int+=9
			# 	i+=2
			# elif s[i]=="V":
			# 	r_int+=5
			# 	i+=1
			# elif s[i]=="I" and  i+1<len(s) and s[i+1]=="V":
			# 	r_int+=4
			# 	i+=2
			# elif s[i]=="I":
			# 	r_int+=1
			# 	i+=1
		return r_int


def main():
	s=Solution()
	print s.romanToInt("MMMCMXCIX")
	pass

if __name__ == '__main__':
	main()