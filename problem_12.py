#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
	def intToRoman(self, num):
	    """
	    :type num: int
	    :rtype: str
	    """
	    #千位
	    roman=""
	    roman_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	    roman_str=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
	    for i in range(len(roman_num)):
	    	temp_num=int(num/roman_num[i])
	    	#print temp_num," ",roman_str[i]," ",num
	    	for j in range(temp_num):
	    		roman+=roman_str[i]
	    	num-=temp_num*roman_num[i]
	    	if num==0:
	    		break
	    
	    return roman
	    pass

def main():
	s=Solution()
	print s.intToRoman(40)
	pass

if __name__ == '__main__':
	main()