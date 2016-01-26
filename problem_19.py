#! /usr/bin/env python
# -*- coding:utf-8 -*-

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		l=0
		current=head
		while current:
			l+=1
			current=current.next
		n=l-n
		if n<0 or n>=l:
			return head
		current=head
		pre=None
		while(n>0 and current):
			n-=1
			pre=current
			current=current.next

		else:
			if pre:
				pre.next=current.next
			else:
				return current.next

		return head

def  main():
	s=Solution()
	l1=ListNode(1)
	l2=ListNode(2)
	l3=ListNode(3)
	l4=ListNode(4)
	l5=ListNode(5)

	l1.next=l2
	l2.next=l3
	l3.next=l4
	l4.next=l5

	l=s.removeNthFromEnd(l1,7)

	while l:
		print l.val
		l=l.next

if __name__ == '__main__':
	main()