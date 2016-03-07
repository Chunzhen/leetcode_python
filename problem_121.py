#! /usr/bin/env python 
#! -*- coding:utf-8 -*-

class Solution(object):
	def maxProfit(self,prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices)<2:
			return 0
		p_max=prices[-1]
		p_min=prices[-1]
		profit=0
		for i in range(len(prices)-2,-1,-1):
			if prices[i]>p_max:
				t=p_max-p_min
				if profit<t:
					profit=t
				p_min=prices[i]
				p_max=prices[i]
			if prices[i]<p_min:
				p_min=prices[i]
		t=p_max-p_min
		if profit<t:
			profit=t
		return profit



def main():
	nums=[1,2,4,6,4,2,2,4,1]
	s=Solution()
	print s.maxProfit(nums)
	pass

if __name__ == '__main__':
	main()