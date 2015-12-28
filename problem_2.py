#! /usr/bin/env python
# -*- coding:utf-8 -*-

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2
        if not l2:
        	return l1

        l=None
        l_next=None
        plus=0
        while l1:
        	if l2:
        		temp=l1.val+l2.val+plus
        	else:
        		temp=l1.val+plus

        	plus=int(temp/10)
        	temp=temp%10
        	t=ListNode(temp)
        	if not l:
        		l=t
        		l_next=l
        	else:
        		l_next.next=t
        		l_next=t

        	l1=l1.next
        	if l2:
        		l2=l2.next

        while l2:
        	temp=l2.val+plus
        	plus=int(temp/10)
        	temp=temp%10
        	t=ListNode(temp)
        	l_next.next=t
        	l_next=t
        	l2=l2.next

        if plus:
        	t=ListNode(plus)
        	l_next.next=t
        return l


def main():
	l1=ListNode(5)
	l2=ListNode(8)
	l3=ListNode(3)
	l4=ListNode(5)
	l5=ListNode(8)
	l6=ListNode(4)

	#l1.next=l2
	# l2.next=l3

	#l4.next=l5
	# l5.next=l6

	s=Solution()
	l=s.addTwoNumbers(l1,l4)

	while l:
		print l.val
		l=l.next



if __name__ == '__main__':
	main()