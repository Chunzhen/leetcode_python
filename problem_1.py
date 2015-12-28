#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
	#解题思路
	#先将数组排序，从最左边开始遍历尝试，如果两个数相加等于target就直接找到nums下的坐标，返回
	#如果大于target，直接break
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

      	nums_set=sorted(nums)

      	for i in range(0,len(nums_set)):
      		for j in range(i+1,len(nums_set)):
      			if nums_set[i]+nums_set[j]==target:
      				l=[]
      				for k,v in enumerate(nums):
      					if nums_set[i]==v:
      						l.append(k+1)
      						break
      				for k,v in enumerate(nums):
      					if nums_set[j]==v and k+1!=l[0]:
      						l.append(k+1)
      						break
      				return sorted(l)
      			elif nums_set[i]+nums_set[j]>target:
      				break


def main():
	solution=Solution()
	nums=[0,4,3,0]
	target=0
	r=solution.twoSum(nums,target)
	print r

if __name__ == '__main__':
  	main()  
